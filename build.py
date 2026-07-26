import json
import os
import shutil
import urllib.parse

# 1. Configuration & Constants
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
DIST_DIR = os.path.join(PROJECT_DIR, "dist")
CSS_DIST_DIR = os.path.join(DIST_DIR, "css")
JS_DIST_DIR = os.path.join(DIST_DIR, "js")

# Breeds list
DOG_BREEDS = [
    "australian-shepherd", "beagle", "bernese-mountain-dog", "border-collie",
    "boston-terrier", "boxer", "bulldog", "cane-corso", "cavapoo",
    "cavalier-king-charles-spaniel", "chihuahua", "cocker-spaniel", "dachshund",
    "doberman-pinscher", "french-bulldog", "german-shepherd", "golden-retriever",
    "great-dane", "labrador-retriever", "maltese", "miniature-schnauzer",
    "pembroke-welsh-corgi", "pomeranian", "poodle", "pug", "rottweiler",
    "shih-tzu", "siberian-husky", "yorkshire-terrier"
]

CAT_BREEDS = [
    "persian", "maine-coon", "ragdoll", "british-shorthair", "siamese", "bengal",
    "scottish-fold", "sphynx", "russian-blue", "norwegian-forest-cat", "siberian", "abyssinian"
]

BREED_SLUGS = DOG_BREEDS + CAT_BREEDS

# Static Content for templates
HERO_IMG = "https://img1.wsimg.com/isteam/getty/2244371184/:/cr=t:0%25,l:12.49%25,w:75.02%25,h:75.02%25"
LOGO_IMG = "https://img1.wsimg.com/isteam/ip/30641560-db5b-4fa9-a2aa-8dbd04b24a5c/images.jpeg"
RETRIEVER_IMG = "https://img1.wsimg.com/isteam/ip/30641560-db5b-4fa9-a2aa-8dbd04b24a5c/IMG_5610.JPG"
SPANIEL_IMG = "https://img1.wsimg.com/isteam/ip/30641560-db5b-4fa9-a2aa-8dbd04b24a5c/Male%20Cocker%20Spaniel%20(Indy).JPG"

MOCK_REVIEWS = [
    {
        "stars": 5,
        "quote": "Adopting our Cavapoo puppy Victoria from Elite Paws was the best decision. The staff was incredibly welcoming, and she is so healthy and happy!",
        "author": "Sarah Jenkins",
        "breed": "Cavapoo"
    },
    {
        "stars": 5,
        "quote": "Incredible breeding standards. Our Doberman Thor is extremely smart, well-socialized, and a gorgeous dog. Highly professional team!",
        "author": "Mark Sterling",
        "breed": "Doberman Pinscher"
    },
    {
        "stars": 5,
        "quote": "We got our little Yorkie Belle last month and she has filled our home with joy. Excellent communication throughout the adoption process.",
        "author": "Lisa & Tom Davis",
        "breed": "Yorkie"
    },
    {
        "stars": 5,
        "quote": "Very clean breeding facilities and healthy parents. Our Chihuahua Tori is a tiny ball of energy. Recommend them to anyone looking for a puppy!",
        "author": "Ashley Cooper",
        "breed": "Chihuahua"
    },
    {
        "stars": 5,
        "quote": "Our Cocker Spaniel puppy has the best temperament! Royal Paws/Heavenly Paws team really knows how to raise happy dogs.",
        "author": "Richard Meyer",
        "breed": "Cocker Spaniel"
    }
]

# Testimonials for the slider section
TESTIMONIALS = [
    {
        "name": "Nomsa T.",
        "location": "Johannesburg, Gauteng",
        "rating": "★★★★★",
        "badge": "Verified Adoption",
        "date": "Adopted January 2026",
        "review": "We adopted a Labrador puppy and the whole process was smooth from start to finish. The puppy was healthy, playful, and clearly well cared for. We couldn’t be happier.",
        "avatar": "images/reviews/review4.jpg"
    },
    {
        "name": "Daniel L.",
        "location": "Cape Town, Western Cape",
        "rating": "★★★★★",
        "badge": "Verified Adoption",
        "date": "Adopted February 2026",
        "review": "Our kitten settled in immediately. The kitten we received was calm, affectionate, and already used to people. The team answered all our questions before delivery. Highly recommended.",
        "avatar": "images/reviews/review5.jpg"
    },
    {
        "name": "Sarah & Michael",
        "location": "Durban, KwaZulu Natal",
        "rating": "★★★★★",
        "badge": "Verified Adoption",
        "date": "Adopted November 2025",
        "review": "We were nervous about buying a puppy online, but everything was transparent. Vaccination records and health information were provided. Excellent service.",
        "avatar": "images/reviews/review3.jpg"
    },
    {
        "name": "Ayesha Z.",
        "location": "Pretoria, Gauteng",
        "rating": "★★★★★",
        "badge": "Verified Adoption",
        "date": "Adopted October 2025",
        "review": "Our puppy arrived energetic and healthy. You can tell the animals are raised with love. We will definitely come back in the future.",
        "avatar": "images/reviews/review1.jpg"
    },
    {
        "name": "Thabo P.",
        "location": "Bloemfontein, Free State",
        "rating": "★★★★★",
        "badge": "Verified Adoption",
        "date": "Adopted December 2025",
        "review": "From the first enquiry to collection day, the communication was excellent. Our family is in love with our new kitten.",
        "avatar": "images/reviews/review2.jpg"
    },
    {
        "name": "Kelebogile E.",
        "location": "Port Elizabeth, Eastern Cape",
        "rating": "★★★★★",
        "badge": "Verified Adoption",
        "date": "Adopted January 2026",
        "review": "The website was easy to use and the photos matched the puppy we received. Thank you for helping us find the perfect companion.",
        "avatar": "https://images.unsplash.com/photo-1531123897727-8f129e1688ce?auto=format&fit=crop&w=150&h=150&q=80"
    },
    {
        "name": "Sarah M.",
        "location": "Cape Town, Western Cape",
        "rating": "★★★★★",
        "badge": "Verified Adoption",
        "date": "Adopted March 2026",
        "review": "Our Golden Retriever settled in from day one. She arrived healthy, playful, and clearly well socialized. Elite Paws kept us updated throughout the process.",
        "avatar": "https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&fit=crop&w=100&h=100&q=80"
    },
    {
        "name": "Daniel N.",
        "location": "Johannesburg, Gauteng",
        "rating": "★★★★☆ (4.5)",
        "badge": "Verified Adoption",
        "date": "Adopted February 2026",
        "review": "Buying a puppy online felt like a big step, but Elite Paws made everything easy. The paperwork was complete and our puppy was exactly as described.",
        "avatar": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=100&h=100&q=80"
    },
    {
        "name": "Lerato K.",
        "location": "Pretoria, Gauteng",
        "rating": "★★★★★",
        "badge": "Verified Adoption",
        "date": "Adopted January 2026",
        "review": "We adopted a Cavapoo for our family and couldn't be happier. The team answered every question before and after delivery.",
        "avatar": "https://images.unsplash.com/photo-1438761681033-6461ffad8d80?auto=format&fit=crop&w=100&h=100&q=80"
    },
    {
        "name": "Michael V.",
        "location": "Durban, KwaZulu Natal",
        "rating": "★★★★★",
        "badge": "Verified Adoption",
        "date": "Adopted April 2026",
        "review": "The communication was excellent. We received vaccination records, health certificates, and regular photo updates before our puppy arrived.",
        "avatar": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=100&h=100&q=80"
    },
    {
        "name": "Amanda P.",
        "location": "Gqeberha, Eastern Cape",
        "rating": "★★★★☆ (4.5)",
        "badge": "Verified Adoption",
        "date": "Adopted December 2025",
        "review": "Our Dachshund is full of energy and has settled in beautifully. You can tell these puppies are raised with care.",
        "avatar": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=100&h=100&q=80"
    },
    {
        "name": "Sipho D.",
        "location": "Bloemfontein, Free State",
        "rating": "★★★★★",
        "badge": "Verified Adoption",
        "date": "Adopted May 2026",
        "review": "Elite Paws exceeded our expectations. Professional service from the first enquiry to delivery. We would recommend them without hesitation.",
        "avatar": "https://images.unsplash.com/photo-1522075469751-3a6694fb2f61?auto=format&fit=crop&w=100&h=100&q=80"
    },
    {
        "name": "Rebecca J.",
        "location": "George, Western Cape",
        "rating": "★★★★★",
        "badge": "Verified Adoption",
        "date": "Adopted November 2025",
        "review": "Our Maltese arrived healthy, happy, and already comfortable around children. We appreciated the lifetime support after adoption.",
        "avatar": "https://images.unsplash.com/photo-1544005313-94ddf0286df2?auto=format&fit=crop&w=100&h=100&q=80"
    },
    {
        "name": "Thabo M.",
        "location": "Polokwane, Limpopo",
        "rating": "★★★★☆ (4.5)",
        "badge": "Verified Adoption",
        "date": "Adopted March 2026",
        "review": "The process was smooth from beginning to end. Delivery was on time and our puppy came with all the required documentation.",
        "avatar": "https://images.unsplash.com/photo-1552058544-f2b08422138a?auto=format&fit=crop&w=100&h=100&q=80"
    },
    {
        "name": "Nicole S.",
        "location": "Mbombela, Mpumalanga",
        "rating": "★★★★★",
        "badge": "Verified Adoption",
        "date": "Adopted June 2026",
        "review": "We adopted a Cavalier King Charles Spaniel and couldn't be happier. Healthy, affectionate, and exactly what we hoped for.",
        "avatar": "https://images.unsplash.com/photo-1580489944761-15a19d654956?auto=format&fit=crop&w=100&h=100&q=80"
    },
    {
        "name": "Johan B.",
        "location": "Kimberley, Northern Cape",
        "rating": "★★★★★",
        "badge": "Verified Adoption",
        "date": "Adopted October 2025",
        "review": "The customer support was outstanding. They checked in after adoption and offered helpful advice while our puppy adjusted to his new home.",
        "avatar": "https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?auto=format&fit=crop&w=100&h=100&q=80"
    },
    {
        "name": "Zanele R.",
        "location": "East London, Eastern Cape",
        "rating": "★★★★★",
        "badge": "Verified Adoption",
        "date": "Adopted February 2026",
        "review": "Everything was handled professionally. From health checks to transport, Elite Paws made the experience stress free.",
        "avatar": "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?auto=format&fit=crop&w=100&h=100&q=80"
    },
    {
        "name": "Chris W.",
        "location": "Stellenbosch, Western Cape",
        "rating": "★★★★☆ (4.5)",
        "badge": "Verified Adoption",
        "date": "Adopted January 2026",
        "review": "Our English Bulldog has become the heart of our family. Friendly service, healthy puppy, and excellent communication throughout.",
        "avatar": "https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?auto=format&fit=crop&w=100&h=100&q=80"
    }
]

# 2. Setup Directories
os.makedirs(DIST_DIR, exist_ok=True)
os.makedirs(CSS_DIST_DIR, exist_ok=True)
os.makedirs(JS_DIST_DIR, exist_ok=True)

# Copy CSS and JS assets
shutil.copy(os.path.join(PROJECT_DIR, "css", "styles.css"), os.path.join(CSS_DIST_DIR, "styles.css"))
shutil.copy(os.path.join(PROJECT_DIR, "js", "app.js"), os.path.join(JS_DIST_DIR, "app.js"))

# Copy images directory recursively
images_src = os.path.join(PROJECT_DIR, "images")
if os.path.exists(images_src):
    images_dst = os.path.join(DIST_DIR, "images")
    if os.path.exists(images_dst):
        shutil.rmtree(images_dst)
    shutil.copytree(images_src, images_dst)

# 3. Load Puppies Database
db_path = os.path.join(PROJECT_DIR, "puppies_db.json")
if not os.path.exists(db_path):
    print("Error: puppies_db.json not found!")
    exit(1)

with open(db_path, "r", encoding="utf-8") as f:
    puppies_db = json.load(f)

# Helper to format breed names
def get_breed_name(slug):
    return puppies_db.get(slug, {}).get("breed_name", slug.replace("-", " ").title())

# Helper to build WhatsApp Message Link
def build_whatsapp_link(puppy_name, breed_name):
    base = "https://wa.me/27715371454"
    msg = f"Hi! I am interested in adopting {puppy_name}, the adorable {breed_name} puppy I saw on your website!"
    return f"{base}?text={urllib.parse.quote(msg)}"

# Helper to clean up puppy name and gender, suggesting values if they are Unknown
def clean_pup_record(pup, index):
    name = pup.get("name", "Unknown")
    gender = pup.get("gender", "Unknown")
    
    if name == "Unknown" or not name:
        import urllib.parse
        import re
        decoded = urllib.parse.unquote(pup.get("src", ""))
        match = re.search(r'\(([^).]+)', decoded)
        if match:
            name = match.group(1).title()
            
    # Adorable suggested names for puppies/kittens if still "Unknown"
    suggested_names = [
        "Bella", "Charlie", "Luna", "Cooper", "Daisy", "Milo", "Lucy", "Rocky", "Lola", "Teddy",
        "Sadie", "Max", "Bailey", "Molly", "Buster", "Sophie", "Buddy", "Coco", "Oliver", "Ruby",
        "Toby", "Chloe", "Duke", "Gigi", "Finn", "Penny", "Zeus", "Lily", "Nala", "Simba",
        "Winston", "Rosie", "Sammy", "Harley", "Stella", "Gizmo", "Ziggy", "Cleo", "Jasper", "Leo"
    ]
    
    if name == "Unknown" or not name:
        # Pick name deterministically based on index so it is consistent
        name = suggested_names[index % len(suggested_names)]
        
    if gender == "Unknown" or not gender or gender.lower() == "unknown":
        # Suggest gender deterministically based on index
        gender = "Male" if index % 2 == 0 else "Female"
        
    return name, gender


# 4. Shared HTML Templates
def get_head(title_suffix):
    title = f"Elite Paws | {title_suffix}"
    return f"""<!DOCTYPE html>
<html lang="en-IE">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="Premium luxury dog and cat breeder. Ethically raised, vet certified, and healthy pets for loving families.">
    <meta name="author" content="Elite Paws">
    <link rel="icon" href="{LOGO_IMG}" type="image/x-icon">
    <link rel="stylesheet" href="css/styles.css?v=30.0">
</head>
<body>
"""

def get_header(active_page):
    def check_active(page):
        return "active" if active_page == page else ""
    
    # Breed dropdown HTML
    sorted_dogs = sorted(DOG_BREEDS, key=lambda x: get_breed_name(x))
    sorted_cats = sorted(CAT_BREEDS, key=lambda x: get_breed_name(x))
    
    dogs_split = (len(sorted_dogs) + 1) // 2
    dogs_col1_html = ""
    for slug in sorted_dogs[:dogs_split]:
        name = get_breed_name(slug)
        dogs_col1_html += f'<li><a href="available-puppies.html?breed={slug}" class="dropdown-link">{name}</a></li>\n'
        
    dogs_col2_html = ""
    for slug in sorted_dogs[dogs_split:]:
        name = get_breed_name(slug)
        dogs_col2_html += f'<li><a href="available-puppies.html?breed={slug}" class="dropdown-link">{name}</a></li>\n'
        
    cats_html = ""
    for slug in sorted_cats:
        name = get_breed_name(slug)
        cats_html += f'<li><a href="available-kittens.html?breed={slug}" class="dropdown-link">{name}</a></li>\n'

    return f"""
    <!-- Site Navigation Header -->
    <header class="site-header">
        <div class="container header-container">
            <a href="index.html" class="logo-link">
                <span class="logo-wrapper">
                    <span class="logo-text">Elite Paws</span>
                    <img src="images/logo-paw.png" alt="Elite Paws Logo" class="logo-paw-icon">
                </span>
            </a>
            
            <nav class="nav-menu">
                <a href="index.html" class="nav-link {check_active('home')}">Home</a>
                <a href="available-puppies.html" class="nav-link {check_active('puppies')}">Puppies</a>
                <a href="available-kittens.html" class="nav-link {check_active('kittens')}">Kittens</a>
                
                <div class="nav-item-dropdown">
                    <a href="#" class="nav-link {check_active('breeds')}">Breeds</a>
                    <div class="dropdown-menu megamenu">
                        <div class="megamenu-section">
                            <h4 class="megamenu-title">Puppy Breeds</h4>
                            <div class="megamenu-columns-wrap">
                                <ul class="megamenu-list">
                                    {dogs_col1_html}
                                </ul>
                                <ul class="megamenu-list">
                                    {dogs_col2_html}
                                </ul>
                            </div>
                        </div>
                        <div class="megamenu-section separator">
                            <h4 class="megamenu-title">Kitty Breeds</h4>
                            <ul class="megamenu-list">
                                {cats_html}
                            </ul>
                        </div>
                    </div>
                </div>
                
                <!-- Mobile-only Contact Us button inside drawer -->
                <a href="contact-us.html" class="nav-contact-btn mobile-only">Contact Us</a>
            </nav>

            <!-- Desktop-only Contact Us button on the right side of the navbar -->
            <div class="nav-actions desktop-only">
                <a href="contact-us.html" class="nav-contact-btn">Contact Us</a>
            </div>
            
            <button class="hamburger" aria-label="Toggle Navigation">
                <span></span>
                <span></span>
                <span></span>
            </button>
        </div>
    </header>
    
    <main class="main-content">
"""

def get_footer():
    return f"""
    </main>
    
    <!-- Footer Section -->
    <footer class="site-footer">
        <div class="container footer-grid">
            <div>
                <a href="index.html" class="logo-link" style="text-decoration: none; margin-bottom: var(--spacing-sm); display: inline-flex;">
                    <span class="logo-wrapper">
                        <span class="logo-text" style="color: var(--color-white); font-size: 32px; line-height: 40px;">Elite Paws</span>
                        <img src="images/logo-paw.png" alt="Elite Paws Logo" class="logo-paw-icon" style="width: 24px; margin-top: -8px;">
                    </span>
                </a>
                <p class="footer-desc">Premium luxury dog and cat breeder. Ethically raised, vet certified, and healthy pets for loving families. We treat your pets like our own family, backing our service with decades of experience.</p>
            </div>
            <div>
                <h4 class="footer-title">Quick Links</h4>
                <ul class="footer-links">
                    <li><a href="available-puppies.html">Available Puppies</a></li>
                    <li><a href="available-kittens.html">Available Kittens</a></li>
                    <li><a href="reviews.html">Pawsome Reviews</a></li>
                    <li><a href="contact-us.html">Contact Us</a></li>
                </ul>
            </div>
            <div>
                <h4 class="footer-title">Popular Breeds</h4>
                <ul class="footer-links">
                    <li><a href="available-kittens.html?breed=british-shorthair">British Shorthair</a></li>
                    <li><a href="available-kittens.html?breed=ragdoll">Ragdoll</a></li>
                    <li><a href="available-puppies.html?breed=labrador-retriever">Labrador Retriever</a></li>
                    <li><a href="available-puppies.html?breed=cavalier-king-charles-spaniel">Cavalier King Charles</a></li>
                </ul>
            </div>
        </div>
        <div class="container footer-bottom">
            <p>Copyright &copy; 2026 Elite Paws - All Rights Reserved.</p>
            <p>Made with love in South Africa 🐾</p>
        </div>
    </footer>

    <!-- Floating WhatsApp Action -->
    <a href="https://wa.me/27715371454" class="whatsapp-sticky" target="_blank" aria-label="Chat on WhatsApp">
        <svg viewBox="0 0 448 512"><path d="M380.9 97.1C339 55.1 283.2 32 223.9 32c-122.4 0-222 99.6-222 222 0 39.1 10.2 77.3 29.6 111L3 496l133.9-35.1c32.7 17.9 69.6 27.3 107.1 27.3 122.4 0 222-99.6 222-222 0-59.3-23.2-115-65.1-157.1zM223.9 448c-33.2 0-65.7-8.9-94-25.7l-6.7-4-79.8 20.9 21.3-77.8-4.4-7c-18.5-29.4-28.2-63.3-28.2-98.2 0-101.7 82.8-184.5 184.6-184.5 49.3 0 95.6 19.2 130.4 54.1 34.8 34.9 54 81.2 54 130.4 0 101.7-82.8 184.5-184.6 184.5zm100.5-137.5c-5.5-2.7-32.6-16.1-37.7-17.9-5.1-1.8-8.8-2.7-12.5 2.7-3.7 5.5-14.3 17.9-17.6 21.5-3.3 3.7-6.6 4.1-12.1 1.4-5.5-2.7-23.2-8.5-44.2-27.1-16.4-14.6-27.4-32.7-30.6-38.2-3.3-5.5-.3-8.5 2.4-11.2 2.5-2.4 5.5-6.4 8.2-9.6 2.7-3.3 3.7-5.5 5.5-9.1 1.8-3.7.9-6.9-.5-9.6-1.4-2.7-12.5-30.1-17.1-41.2-4.5-10.8-9.1-9.3-12.5-9.5-3.2-.2-6.9-.2-10.6-.2-3.7 0-9.7 1.4-14.8 6.9-5.1 5.5-19.4 19-19.4 46.3 0 27.3 19.9 53.7 22.6 57.4 2.8 3.7 39.1 59.7 94.8 83.8 13.3 5.7 23.6 9.2 31.6 11.7 13.3 4.2 25.4 3.6 35 2.2 10.7-1.6 32.6-13.3 37.2-26.2 4.6-12.9 4.6-24 3.2-26.2-1.3-2.2-5-3.5-10.5-6.2z"/></svg>
    </a>

    <!-- Cookie Consent Banner -->
    <div class="cookie-banner">
        <h4 class="cookie-title">This website uses cookies.</h4>
        <p class="cookie-desc">We use cookies to analyze website traffic and optimize your website experience. By accepting our use of cookies, your data will be aggregated with all other user data.</p>
        <div class="cookie-btn-wrap">
            <button class="cookie-accept-btn">Accept Cookies</button>
        </div>
    </div>

    <!-- Client JS -->
    <script src="js/app.js"></script>
</body>
</html>
"""

# 5. Build Homepage (index.html)
def build_homepage():
    # Fetch 4 featured puppy cards
    featured_puppy_cards = ""
    count = 0
    featured_slugs = ["beagle", "yorkshire-terrier", "rottweiler", "dachshund"]
    for slug in featured_slugs:
        data = puppies_db.get(slug, {})
        pups = data.get("puppies", [])
        if pups:
            pup = pups[0]
            pup_name, pup_gender = clean_pup_record(pup, count)
            gender_class = pup_gender.lower()
            featured_puppy_cards += f"""
            <div class="puppy-card" data-breed="{slug}" data-gender="{gender_class}">
                <div class="puppy-img-wrap">
                    <img src="{pup['src']}" alt="{pup['alt']}" class="puppy-img" loading="lazy">
                </div>
                <div class="puppy-info">
                    <div class="puppy-card-details">
                        <div class="puppy-detail-item">
                            <span class="puppy-detail-label">Name</span>
                            <span style="font-weight: 700;">{pup_name}</span>
                        </div>
                        <div class="puppy-detail-item">
                            <span class="puppy-detail-label">Breed</span>
                            <span style="font-weight: 600;">{data['breed_name']}</span>
                        </div>
                        <div class="puppy-detail-item">
                            <span class="puppy-detail-label">Gender</span>
                            <span>{pup_gender}</span>
                        </div>
                        <div class="puppy-detail-item">
                            <span class="puppy-detail-label">Status</span>
                            <span class="puppy-status-available" style="color: #339e45; font-weight: 700;">Available</span>
                        </div>
                        <div class="puppy-detail-item">
                            <span class="puppy-detail-label">Delivery</span>
                            <span>Nationwide</span>
                        </div>
                        <div class="puppy-detail-item">
                            <span class="puppy-detail-label">Health</span>
                            <span>Vet Checked</span>
                        </div>
                        <div class="puppy-detail-item">
                            <span class="puppy-detail-label">Vaccinations</span>
                            <span>Up to Date</span>
                        </div>
                        <div class="puppy-detail-item">
                            <span class="puppy-detail-label">Registration</span>
                            <span>Documents Included</span>
                        </div>
                    </div>
                    <a href="contact-us.html" class="puppy-inquiry-btn">
                        Buy me
                    </a>
                </div>
            </div>
            """
            count += 1

    # Fetch 4 featured kitten cards
    featured_kitten_cards = ""
    count = 0
    for slug in CAT_BREEDS:
        if count >= 4:
            break
        data = puppies_db.get(slug, {})
        kits = data.get("puppies", [])
        if kits:
            kit = kits[0]
            kit_name, kit_gender = clean_pup_record(kit, count)
            gender_class = kit_gender.lower()
            featured_kitten_cards += f"""
            <div class="puppy-card" data-breed="{slug}" data-gender="{gender_class}">
                <div class="puppy-img-wrap">
                    <img src="{kit['src']}" alt="{kit['alt']}" class="puppy-img" loading="lazy">
                </div>
                <div class="puppy-info">
                    <div class="puppy-card-details">
                        <div class="puppy-detail-item">
                            <span class="puppy-detail-label">Name</span>
                            <span style="font-weight: 700;">{kit_name}</span>
                        </div>
                        <div class="puppy-detail-item">
                            <span class="puppy-detail-label">Breed</span>
                            <span style="font-weight: 600;">{data['breed_name']}</span>
                        </div>
                        <div class="puppy-detail-item">
                            <span class="puppy-detail-label">Gender</span>
                            <span>{kit_gender}</span>
                        </div>
                        <div class="puppy-detail-item">
                            <span class="puppy-detail-label">Status</span>
                            <span class="puppy-status-available" style="color: #339e45; font-weight: 700;">Available</span>
                        </div>
                        <div class="puppy-detail-item">
                            <span class="puppy-detail-label">Delivery</span>
                            <span>Nationwide</span>
                        </div>
                        <div class="puppy-detail-item">
                            <span class="puppy-detail-label">Health</span>
                            <span>Vet Checked</span>
                        </div>
                        <div class="puppy-detail-item">
                            <span class="puppy-detail-label">Vaccinations</span>
                            <span>Up to Date</span>
                        </div>
                        <div class="puppy-detail-item">
                            <span class="puppy-detail-label">Registration</span>
                            <span>Documents Included</span>
                        </div>
                    </div>
                    <a href="contact-us.html" class="puppy-inquiry-btn">
                        Buy me
                    </a>
                </div>
            </div>
            """
            count += 1

    # Build testimonials slider cards
    slider_reviews_html = ""
    for idx, t in enumerate(TESTIMONIALS):
        rating_clean = t['rating'].replace(" (4.5)", "").strip()
        slider_reviews_html += f"""
                            <!-- Card {idx + 1} ({t['name']}) -->
                            <div class="review-slider-card dark-card">
                                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: var(--spacing-sm);">
                                    <div class="slider-card-stars">{rating_clean}</div>
                                </div>
                                <p class="slider-card-text">"{t['review']}"</p>
                                <div class="slider-card-author">
                                    <img src="{t['avatar']}" alt="{t['name']}" class="author-avatar">
                                    <div class="author-info-text">
                                        <div class="author-name" style="display: flex; align-items: center; gap: 6px;">
                                            {t['name']}
                                            <svg class="verified-icon" style="width: 20px; height: 20px; fill: #CEC9C1; flex-shrink: 0;" viewBox="0 0 24 24" aria-label="Verified Customer">
                                                <path fill-rule="evenodd" clip-rule="evenodd" d="M15.4181 5.643C15.2801 5.42264 15.077 5.25076 14.8368 5.15128C14.5966 5.05181 14.3314 5.02969 14.0781 5.088L12.2801 5.501C12.0958 5.54335 11.9043 5.54335 11.7201 5.501L9.92205 5.088C9.66872 5.02969 9.4035 5.05181 9.16333 5.15128C8.92315 5.25076 8.71997 5.42264 8.58205 5.643L7.60205 7.207C7.50205 7.367 7.36705 7.502 7.20705 7.603L5.64305 8.583C5.42307 8.72079 5.25144 8.92365 5.15199 9.16341C5.05253 9.40318 5.03019 9.66796 5.08805 9.921L5.50105 11.721C5.54325 11.9049 5.54325 12.0961 5.50105 12.28L5.08805 14.079C5.02996 14.3322 5.0522 14.5972 5.15166 14.8372C5.25112 15.0771 5.42288 15.2802 5.64305 15.418L7.20705 16.398C7.36705 16.498 7.50205 16.633 7.60305 16.793L8.58305 18.357C8.86505 18.808 9.40305 19.031 9.92205 18.912L11.7201 18.499C11.9043 18.4567 12.0958 18.4567 12.2801 18.499L14.0791 18.912C14.3322 18.9701 14.5972 18.9479 14.8372 18.8484C15.0772 18.7489 15.2802 18.5772 15.4181 18.357L16.3981 16.793C16.4981 16.633 16.6331 16.498 16.7931 16.398L18.3581 15.418C18.5782 15.2799 18.7499 15.0767 18.8492 14.8365C18.9485 14.5964 18.9705 14.3312 18.9121 14.078L18.5001 12.28C18.4577 12.0957 18.4577 11.9043 18.5001 11.72L18.9131 9.921C18.9712 9.66792 18.9492 9.40299 18.8499 9.16303C18.7506 8.92307 18.579 8.71999 18.3591 8.582L16.7941 7.602C16.6343 7.50182 16.4992 7.36678 16.3991 7.207L15.4181 5.643ZM14.9151 9.77C14.9769 9.65627 14.9922 9.52298 14.9578 9.39817C14.9234 9.27337 14.8419 9.16679 14.7305 9.10085C14.6191 9.0349 14.4864 9.01475 14.3604 9.04462C14.2345 9.07449 14.125 9.15206 14.0551 9.261L11.4401 13.687L9.86105 12.175C9.81421 12.1269 9.75816 12.0887 9.69624 12.0628C9.63433 12.0368 9.56782 12.0236 9.50068 12.0239C9.43354 12.0241 9.36715 12.038 9.30546 12.0645C9.24377 12.091 9.18806 12.1296 9.14164 12.1781C9.09521 12.2266 9.05903 12.284 9.03526 12.3468C9.01148 12.4096 9.0006 12.4765 9.00325 12.5436C9.0059 12.6107 9.02204 12.6766 9.05069 12.7373C9.07935 12.798 9.11995 12.8523 9.17005 12.897L11.2041 14.846C11.2585 14.8981 11.324 14.9371 11.3956 14.9603C11.4673 14.9835 11.5433 14.9902 11.6179 14.9799C11.6925 14.9696 11.7638 14.9426 11.8265 14.9009C11.8893 14.8592 11.9417 14.8038 11.9801 14.739L14.9151 9.77Z"/>
                                            </svg>
                                        </div>
                                        <div class="author-meta">{t['location']} &bull; {t['date']}</div>
                                    </div>
                                </div>
                            </div>
        """

    home_breed_options = '<option value="General Inquiry">General Inquiry / Other</option>\n'
    for slug in BREED_SLUGS:
        name = get_breed_name(slug)
        home_breed_options += f'<option value="{name}">{name}</option>\n'

    body_content = f"""
    <section class="hero-section">
        <!-- Slideshow Background Images -->
        <div class="hero-slideshow">
            <img src="images/hero-bg-1.jpg" alt="Puppies and Kittens Best Friends" class="hero-bg-img active">
            <img src="images/hero-bg-2.jpg" alt="Puppies and Kittens Best Friends" class="hero-bg-img">
            <img src="images/hero-bg-3.jpg" alt="Puppies and Kittens Best Friends" class="hero-bg-img">
            <img src="images/hero-bg-4.png" alt="Puppies and Kittens Best Friends" class="hero-bg-img">
        </div>
        <div class="hero-overlay"></div>
        <div class="container hero-container-overlay">
            <div class="hero-content">
                <div class="hero-tagline">Family-Owned & Raised with Love</div>
                <h1 class="hero-title">Welcome to Elite Paws</h1>
                <p class="hero-desc">We are premier breeders offering ethically raised, vet-certified puppies and kittens for loving families. Discover your perfect, healthy new family member raised with dedicated care and affection.</p>
                <div class="hero-buttons" style="display: flex; flex-wrap: wrap; gap: 16px;">
                    <a href="available-puppies.html" class="btn-primary">View Puppies</a>
                    <a href="available-kittens.html" class="btn-secondary">View Kittens</a>
                </div>
            </div>
            <!-- Slideshow Indicators -->
            <div class="hero-indicators">
                <span class="indicator active" data-slide="0"></span>
                <span class="indicator" data-slide="1"></span>
                <span class="indicator" data-slide="2"></span>
                <span class="indicator" data-slide="3"></span>
            </div>
        </div>

        <!-- 2. Trusted By Families Section (Overlayed at bottom of Hero) -->
        <div class="trusted-bar">
            <div class="container">
                <div class="trusted-title">Our Trust Guarantees</div>
                <div class="trusted-badges-grid">
                    <div class="trusted-badge-item">
                        <svg viewBox="0 0 24 24"><path d="M12 2C6.5 2 2 6.5 2 12s4.5 10 10 10 10-4.5 10-10S17.5 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/></svg>
                        Health Checked
                    </div>
                    <div class="trusted-badge-item">
                        <svg viewBox="0 0 24 24"><path d="M12 2C6.5 2 2 6.5 2 12s4.5 10 10 10 10-4.5 10-10S17.5 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/></svg>
                        Vet Certified
                    </div>
                    <div class="trusted-badge-item">
                        <svg viewBox="0 0 24 24"><path d="M12 2C6.5 2 2 6.5 2 12s4.5 10 10 10 10-4.5 10-10S17.5 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/></svg>
                        Vaccinated
                    </div>
                    <div class="trusted-badge-item">
                        <svg viewBox="0 0 24 24"><path d="M12 2C6.5 2 2 6.5 2 12s4.5 10 10 10 10-4.5 10-10S17.5 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/></svg>
                        Microchipped
                    </div>
                    <div class="trusted-badge-item">
                        <svg viewBox="0 0 24 24"><path d="M12 2C6.5 2 2 6.5 2 12s4.5 10 10 10 10-4.5 10-10S17.5 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/></svg>
                        Ethically Raised
                    </div>
                    <div class="trusted-badge-item">
                        <svg viewBox="0 0 24 24"><path d="M12 2C6.5 2 2 6.5 2 12s4.5 10 10 10 10-4.5 10-10S17.5 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/></svg>
                        Lifetime Support
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 2.5 About Us Section -->
    <section class="about-us-section reveal">
        <div class="container">
            <div class="about-us-header">
                <span class="about-line"></span>
                <h2 class="about-us-title">About Elite Paws</h2>
                <span class="about-line"></span>
            </div>
            
            <div class="about-us-grid">
                <!-- Column 1 -->
                <div class="about-us-col">
                    <div class="about-img-wrap">
                        <img src="images/about-1.jpg" alt="Warm & Welcoming" class="about-img">
                    </div>
                    <h3 class="about-col-title">Warm & Welcoming</h3>
                    <p class="about-col-desc">Welcome to Elite Paws, where healthy puppies and kittens find loving homes. We are dedicated to raising happy, well cared for companions through responsible breeding, expert care, and plenty of love. From your first enquiry to bringing your new family member home, our team is here to make the experience simple, transparent, and memorable.</p>
                </div>
                
                <!-- Column 2 -->
                <div class="about-us-col">
                    <div class="about-img-wrap">
                        <img src="images/about-2.jpg" alt="Premium & Trustworthy" class="about-img">
                    </div>
                    <h3 class="about-col-title">Premium & Trustworthy</h3>
                    <p class="about-col-desc">At Elite Paws, we believe every family deserves a healthy, happy companion. Our puppies and kittens are ethically raised in a clean, nurturing environment, receive regular veterinary care, and are well socialized before joining their forever homes. We are committed to quality, responsible breeding, and building lasting relationships with every family we serve.</p>
                </div>
                
                <!-- Column 3 -->
                <div class="about-us-col">
                    <div class="about-img-wrap">
                        <img src="images/about-3.jpg" alt="Professional & Confidence Building" class="about-img">
                    </div>
                    <h3 class="about-col-title">Professional & Confidence Building</h3>
                    <p class="about-col-desc">Your confidence starts with our commitment to responsible breeding and exceptional care. Every puppy and kitten at Elite Paws receives routine health checks, age appropriate vaccinations, and daily socialization to ensure they are ready for life with their new family. We focus on raising healthy, confident companions while providing honest guidance and support throughout your adoption journey.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- 3. Available Puppies (Featured Grid) -->
    <section class="section-padding reveal" style="background-color: var(--color-white);">
        <div class="container">
            <div class="section-header">
                <h2 class="section-title">Featured Puppies</h2>
                <p class="section-subtitle">Meet some of our gorgeous available puppies raised in a loving family home.</p>
            </div>
            
            <div class="puppies-grid featured-puppies-grid" style="margin-bottom: 48px;">
                {featured_puppy_cards}
            </div>

            <div style="text-align: center;">
                <a href="available-puppies.html" class="btn-primary">Browse All Available Puppies</a>
            </div>
        </div>
    </section>

    <!-- 4. Available Kittens (Featured Grid) -->
    <section class="section-padding reveal" style="background-color: var(--color-bg-alt);">
        <div class="container">
            <div class="section-header">
                <h2 class="section-title">Featured Kittens</h2>
                <p class="section-subtitle">Discover our highly socialized, beautiful available kittens.</p>
            </div>
            
            <div class="puppies-grid featured-puppies-grid" style="margin-bottom: 48px;">
                {featured_kitten_cards}
            </div>

            <div style="text-align: center;">
                <a href="available-kittens.html" class="btn-primary">Browse All Available Kittens</a>
            </div>
        </div>
    </section>

    <!-- 5. Why Choose Elite Paws -->
    <section class="section-padding reveal" style="background-color: var(--color-white);">
        <div class="container">
            <div class="section-header">
                <h2 class="section-title">Why Choose Elite Paws</h2>
                <p class="section-subtitle">Redefining pet breeding, care, and comfort with a touch of luxury.</p>
            </div>
            
            <div class="about-cards-grid why-choose-grid">
                <div class="about-card why-choose-card">
                    <svg width="72" height="72" viewBox="0 0 64 64" fill="none" stroke="var(--color-primary)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="display: block; margin: 0 auto;">
                        <!-- Roof -->
                        <path d="M10 30 L32 12 L54 30" />
                        <!-- Chimney -->
                        <path d="M46 16.5 L46 22" />
                        <!-- Walls -->
                        <path d="M14 27 L14 50 L50 50 L50 27" />
                        <!-- Heart -->
                        <path d="M32 44 C25.5 37.5 24 33 24 30 C24 26.5 26.5 24 29.5 24 C31 24 32 25 32 25 C32 25 33 24 34.5 24 C37.5 24 40 26.5 40 30 C40 33 38.5 37.5 32 44 Z" />
                        <!-- Paw Print Main Pad -->
                        <path d="M32 37.5 C33.5 37.5 34.5 36.5 34.5 35.5 C34.5 34.5 33.2 33.8 32 33.8 C30.8 33.8 29.5 34.5 29.5 35.5 C29.5 36.5 30.5 37.5 32 37.5 Z" fill="var(--color-primary)" stroke="none" />
                        <!-- Paw Print Toes -->
                        <circle cx="28.2" cy="32.8" r="1" fill="var(--color-primary)" stroke="none" />
                        <circle cx="30.5" cy="31" r="1" fill="var(--color-primary)" stroke="none" />
                        <circle cx="33.5" cy="31" r="1" fill="var(--color-primary)" stroke="none" />
                        <circle cx="35.8" cy="32.8" r="1" fill="var(--color-primary)" stroke="none" />
                    </svg>
                    <h3 class="about-card-title">Ethically Raised</h3>
                    <p class="about-card-desc">All our animals are raised in a spacious, clean, and loving family environment, with plenty of socialization from day one.</p>
                </div>
                <div class="about-card why-choose-card">
                    <svg width="72" height="72" viewBox="0 0 64 64" fill="none" stroke="var(--color-primary)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="display: block; margin: 0 auto;">
                        <!-- Inner Shield -->
                        <path d="M32 48 C41.5 43.5 43.5 33.5 43.5 25.5 L43.5 21 L32 17 L20.5 21 L20.5 25.5 C20.5 33.5 22.5 43.5 32 48 Z" />
                        <!-- Outer Shield -->
                        <path d="M32 52 C44 47.5 46.5 36 46.5 27 L46.5 18 L32 13 L17.5 18 L17.5 27 C17.5 36 20 47.5 32 52 Z" />
                        <!-- Checkmark -->
                        <path d="M26 31.5 L30 35.5 L38 27.5" stroke-width="2.5" />
                    </svg>
                    <h3 class="about-card-title">Vet Certified</h3>
                    <p class="about-card-desc">Every puppy and kitten is vet-certified, fully vaccinated, dewormed, and microchipped before arriving at their new home.</p>
                </div>
                <div class="about-card why-choose-card">
                    <svg width="72" height="72" viewBox="0 0 64 64" fill="none" stroke="var(--color-primary)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="display: block; margin: 0 auto;">
                        <!-- Headband -->
                        <path d="M18 32 C18 22 24 16 32 16 C40 16 46 22 46 32" stroke-width="2.5" />
                        <!-- Left Cushion -->
                        <rect x="14" y="28" width="4" height="10" rx="2" />
                        <path d="M18 26 L18 40" />
                        <!-- Right Cushion -->
                        <rect x="46" y="28" width="4" height="10" rx="2" />
                        <path d="M46 26 L46 40" />
                        <!-- Earcup Outer Connectors -->
                        <path d="M16 28 C16 28 12 30 12 33 L12 35 C12 38 16 40 16 40" />
                        <path d="M48 28 C48 28 52 30 52 33 L52 35 C52 38 48 40 48 40" />
                        <path d="M50 38 L50 43" />
                        <!-- Mic Arm -->
                        <path d="M16 38 C16 44 24 47 34 47 C37 47 38 45.5 38 45.5" />
                        <!-- Mic Tip -->
                        <rect x="38" y="44" width="6" height="3" rx="1.5" fill="var(--color-primary)" stroke="none" />
                    </svg>
                    <h3 class="about-card-title">Lifetime Support</h3>
                    <p class="about-card-desc">We offer continuous advice and support to our adoptive families, helping you navigate training, diet, and general pet wellness.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- 6. Testimonials Showcase Section -->
    <section class="reviews-showcase-section reveal">
        <div class="container">
            <div class="dark-testimonials-box">
                <!-- Top Header & Stats Grid -->
                <div class="dark-testimonials-header">
                    <!-- Left Stat Block -->
                    <div class="testimonials-stat-block">
                        <div class="stat-big-number">500+</div>
                        <div class="stat-ratings-wrap">
                            <div class="avatar-bubbles">
                                <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=100&h=100&q=80" alt="Pet Owner" class="avatar-bubble">
                                <img src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=100&h=100&q=80" alt="Pet Owner" class="avatar-bubble">
                                <img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&fit=crop&w=100&h=100&q=80" alt="Pet Owner" class="avatar-bubble">
                            </div>
                            <div class="ratings-text-block">
                                <div class="rating-stars-row">
                                    <span class="rating-value">4.9</span>
                                    <span class="green-stars">★★★★★</span>
                                </div>
                                <div class="rating-subtext">Based on 500+ reviews</div>
                            </div>
                        </div>
                    </div>

                    <!-- Right Header Block -->
                    <div class="testimonials-text-block">
                        <div class="testimonials-label">Testimonials</div>
                        <h2 class="dark-heading">Loved by <span class="italic-serif">pet families</span> across South Africa</h2>
                    </div>
                </div>

                <!-- Slider Wrapper -->
                <div class="slider-container-relative">
                    <div class="reviews-slider-wrap" id="home-reviews-slider-wrap">
                        <div class="reviews-slider">
{slider_reviews_html}
                        </div>
                    </div>

                    <!-- Slider Navigation Controls -->
                    <div class="slider-controls-wrap">
                        <button class="slider-control-btn btn-prev" id="reviews-prev-btn" aria-label="Previous Review">←</button>
                        <button class="slider-control-btn btn-next" id="reviews-next-btn" aria-label="Next Review">→</button>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 8. Frequently Asked Questions Section -->
    <section class="section-padding faq-section reveal">
        <div class="container">
            <div class="section-header">
                <h2 class="section-title">Frequently Asked Questions</h2>
                <p class="section-subtitle">Answers to common questions about adopting from Elite Paws.</p>
            </div>
            <div class="faq-list">
                <div class="faq-item">
                    <button class="faq-question">
                        <span>How does the adoption process work?</span>
                        <span class="faq-icon">+</span>
                    </button>
                    <div class="faq-answer">
                        <p>Simply select your favorite available puppy or kitten, click "WhatsApp Adopt" to connect with us, and we will guide you through reservation, health screening, and safe delivery/collection.</p>
                    </div>
                </div>
                <div class="faq-item">
                    <button class="faq-question">
                        <span>Are the pets vaccinated and microchipped?</span>
                        <span class="faq-icon">+</span>
                    </button>
                    <div class="faq-answer">
                        <p>Yes, absolutely. All puppies and kittens are vaccinated up to their age, microchipped, dewormed regularly, and come with their official veterinary health booklet.</p>
                    </div>
                </div>
                <div class="faq-item">
                    <button class="faq-question">
                        <span>Do you deliver across South Africa?</span>
                        <span class="faq-icon">+</span>
                    </button>
                    <div class="faq-answer">
                        <p>Yes. We organize secure, climate-controlled pet travel and shipping via professional pet couriers to Cape Town, Johannesburg, Durban, Pretoria, and other major cities.</p>
                    </div>
                </div>
                <div class="faq-item">
                    <button class="faq-question">
                        <span>What support do you offer post-adoption?</span>
                        <span class="faq-icon">+</span>
                    </button>
                    <div class="faq-answer">
                        <p>We offer lifetime support. You can message us anytime via WhatsApp with questions regarding diet, training, socialization, or general wellness advice.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 9. Contact Section -->
    <section class="section-padding reveal" style="background-color: var(--color-bg-main); color: var(--color-headings); padding: 6rem 0; font-family: var(--font-body);" id="contact-us-section">
        <div class="container">
            <!-- Centered Header with Lines -->
            <div style="display: flex; align-items: center; justify-content: center; margin-bottom: 5rem;">
                <div style="flex-grow: 1; height: 1px; background-color: var(--color-border); max-width: 35%;"></div>
                <h2 style="font-family: var(--font-headings); font-size: 2.5rem; font-weight: normal; margin: 0 2rem; color: var(--color-headings); white-space: nowrap; letter-spacing: 1px;">Get in Touch</h2>
                <div style="flex-grow: 1; height: 1px; background-color: var(--color-border); max-width: 35%;"></div>
            </div>

            <div class="contact-grid" style="display: grid; grid-template-columns: 1fr 1.1fr; gap: 5rem; align-items: start;">
                
                <!-- Left Column (WhatsApp Info) -->
                <div style="display: flex; flex-direction: column; align-items: flex-start; gap: 20px;">
                    <h2 style="font-family: var(--font-headings); font-size: 2rem; font-weight: normal; color: var(--color-headings); margin: 0 0 10px 0; line-height: 1.3;">Better yet, see us in person!</h2>
                    <p style="color: var(--color-text-main); font-size: 1rem; margin-bottom: 25px; line-height: 1.6; max-width: 480px;">
                        We love our customers, so feel free to visit during normal business hours.
                    </p>
                    
                    <a href="https://wa.me/27715371454" target="_blank" style="background-color: #FFFFFF; color: #1F2937; border-radius: 50px; padding: 12px 28px; font-weight: 700; font-size: 0.95rem; display: inline-flex; align-items: center; gap: 10px; text-decoration: none; transition: transform 0.2s, box-shadow 0.2s; border: 1px solid rgba(0,0,0,0.1); box-shadow: 0 4px 15px rgba(0,0,0,0.06); margin-bottom: 40px;" onmouseover="this.style.transform='translateY(-2px)'" onmouseout="this.style.transform='translateY(0)'">
                        <!-- Green WhatsApp Icon -->
                        <svg style="width: 20px; height: 20px; fill: #25D366; flex-shrink: 0;" viewBox="0 0 448 512">
                            <path d="M380.9 97.1C339 55.1 283.2 32 223.9 32c-122.4 0-222 99.6-222 222 0 39.1 10.2 77.3 29.6 111L3 496l133.9-35.1c32.7 17.9 69.6 27.3 107.1 27.3 122.4 0 222-99.6 222-222 0-59.3-23.2-115-65.1-157.1zM223.9 448c-33.2 0-65.7-8.9-94-25.7l-6.7-4-79.8 20.9 21.3-77.8-4.4-7c-18.5-29.4-28.2-63.3-28.2-98.2 0-101.7 82.8-184.5 184.6-184.5 49.3 0 95.6 19.2 130.4 54.1 34.8 34.9 54 81.2 54 130.4 0 101.7-82.8 184.5-184.6 184.5zm100.5-137.5c-5.5-2.7-32.6-16.1-37.7-17.9-5.1-1.8-8.8-2.7-12.5 2.7-3.7 5.5-14.3 17.9-17.6 21.5-3.3 3.7-6.6 4.1-12.1 1.4-5.5-2.7-23.2-8.5-44.2-27.1-16.4-14.6-27.4-32.7-30.6-38.2-3.3-5.5-.3-8.5 2.4-11.2 2.5-2.4 5.5-6.4 8.2-9.6 2.7-3.3 3.7-5.5 5.5-9.1 1.8-3.7.9-6.9-.5-9.6-1.4-2.7-12.5-30.1-17.1-41.2-4.5-10.8-9.1-9.3-12.5-9.5-3.2-.2-6.9-.2-10.6-.2-3.7 0-9.7 1.4-14.8 6.9-5.1 5.5-19.4 19-19.4 46.3 0 27.3 19.9 53.7 22.6 57.4 2.8 3.7 39.1 59.7 94.8 83.8 13.3 5.7 23.6 9.2 31.6 11.7 13.3 4.2 25.4 3.6 35 2.2 10.7-1.6 32.6-13.3 37.2-26.2 4.6-12.9 4.6-24 3.2-26.2-1.3-2.2-5-3.5-10.5-6.2z"/>
                        </svg>
                        Message us on WhatsApp
                    </a>
                    
                    <div style="font-family: var(--font-headings); font-size: 1.6rem; font-weight: normal; color: var(--color-headings); letter-spacing: 0.5px;">Heavenly Paws Place</div>
                </div>

                <!-- Right Column (Contact Form) -->
                <div style="display: flex; flex-direction: column; gap: 20px; width: 100%;">
                    <h2 style="font-family: var(--font-headings); font-size: 2rem; font-weight: normal; color: var(--color-headings); margin: 0 0 10px 0; line-height: 1.3;">Drop us a line!</h2>
                    
                    <form id="contact-form" style="display: flex; flex-direction: column; gap: 15px; width: 100%;">
                        <!-- Form Inputs Outline Design -->
                        <div style="display: flex; flex-direction: column; gap: 16px;">
                            <input type="text" id="form-name" required placeholder="Name" 
                                style="width: 100%; padding: 14px 18px; background-color: var(--color-white); border: 1px solid var(--color-border); border-radius: 6px; color: var(--color-headings); font-size: 1rem; font-family: var(--font-body); outline: none; transition: border-color 0.2s;"
                                onfocus="this.style.borderColor='var(--color-primary)'" onblur="this.style.borderColor='var(--color-border)'">
                            
                            <input type="email" id="form-email" required placeholder="Email*" 
                                style="width: 100%; padding: 14px 18px; background-color: var(--color-white); border: 1px solid var(--color-border); border-radius: 6px; color: var(--color-headings); font-size: 1rem; font-family: var(--font-body); outline: none; transition: border-color 0.2s;"
                                onfocus="this.style.borderColor='var(--color-primary)'" onblur="this.style.borderColor='var(--color-border)'">
                            
                            <input type="tel" id="form-whatsapp" required placeholder="WhatsApp Only*" 
                                style="width: 100%; padding: 14px 18px; background-color: var(--color-white); border: 1px solid var(--color-border); border-radius: 6px; color: var(--color-headings); font-size: 1rem; font-family: var(--font-body); outline: none; transition: border-color 0.2s;"
                                onfocus="this.style.borderColor='var(--color-primary)'" onblur="this.style.borderColor='var(--color-border)'">
                            
                            <input type="text" id="form-puppy" required placeholder="Interested Puppy's Name*" 
                                style="width: 100%; padding: 14px 18px; background-color: var(--color-white); border: 1px solid var(--color-border); border-radius: 6px; color: var(--color-headings); font-size: 1rem; font-family: var(--font-body); outline: none; transition: border-color 0.2s;"
                                onfocus="this.style.borderColor='var(--color-primary)'" onblur="this.style.borderColor='var(--color-border)'">
                            
                            <input type="text" id="form-breed" placeholder="Interested Puppy's Breed" 
                                style="width: 100%; padding: 14px 18px; background-color: var(--color-white); border: 1px solid var(--color-border); border-radius: 6px; color: var(--color-headings); font-size: 1rem; font-family: var(--font-body); outline: none; transition: border-color 0.2s;"
                                onfocus="this.style.borderColor='var(--color-primary)'" onblur="this.style.borderColor='var(--color-border)'">
                            
                            <input type="text" id="form-province" required placeholder="Province*" 
                                style="width: 100%; padding: 14px 18px; background-color: var(--color-white); border: 1px solid var(--color-border); border-radius: 6px; color: var(--color-headings); font-size: 1rem; font-family: var(--font-body); outline: none; transition: border-color 0.2s;"
                                onfocus="this.style.borderColor='var(--color-primary)'" onblur="this.style.borderColor='var(--color-border)'">
                            
                            <textarea id="form-msg" required placeholder="Message*" rows="5"
                                style="width: 100%; padding: 14px 18px; background-color: var(--color-white); border: 1px solid var(--color-border); border-radius: 6px; color: var(--color-headings); font-size: 1rem; font-family: var(--font-body); outline: none; resize: vertical; transition: border-color 0.2s;"
                                onfocus="this.style.borderColor='var(--color-primary)'" onblur="this.style.borderColor='var(--color-border)'"></textarea>
                        </div>

                        <!-- Rounded Grey Pill Send Button -->
                        <button type="submit" class="contact-send-btn" 
                            style="width: 100%; background-color: #6B7280; color: #FFFFFF; border: none; border-radius: 50px; padding: 14px 28px; font-weight: 600; font-size: 1.05rem; cursor: pointer; transition: background-color 0.2s, transform 0.1s;"
                            onmouseover="this.style.backgroundColor='#4B5563'" onmouseout="this.style.backgroundColor='#6B7280'"
                            onmousedown="this.style.transform='scale(0.98)'" onmouseup="this.style.transform='scale(1)'">
                            Send
                        </button>
                        
                        <!-- Footnote -->
                        <p style="font-size: 0.75rem; color: var(--color-text-light); text-align: center; margin-top: 15px; line-height: 1.4; font-family: var(--font-body);">
                            This site is protected by reCAPTCHA and the Google <a href="https://policies.google.com/privacy" target="_blank" style="color: var(--color-text-light); text-decoration: underline;">Privacy Policy</a> and <a href="https://policies.google.com/terms" target="_blank" style="color: var(--color-text-light); text-decoration: underline;">Terms of Service</a> apply.
                        </p>
                    </form>
                </div>

            </div>
        </div>
    </section>
    """
    
    html = get_head("Home") + get_header("home") + body_content + get_footer()
    with open(os.path.join(DIST_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)

# 6. Build Available Puppies (available-puppies.html)
def build_puppies_page():
    # Gather only puppies from dog breeds
    all_puppies = []
    for slug in DOG_BREEDS:
        data = puppies_db.get(slug, {})
        for pup in data.get("puppies", []):
            all_puppies.append({
                "breed_slug": slug,
                "breed_name": data["breed_name"],
                "name": pup["name"],
                "alt": pup["alt"],
                "src": pup["src"],
                "gender": pup["gender"]
            })

    # Breed filter buttons HTML
    breed_buttons = '<button class="filter-btn active" data-breed="all">All Breeds</button>\n'
    for slug in DOG_BREEDS:
        name = get_breed_name(slug)
        breed_buttons += f'<button class="filter-btn" data-breed="{slug}">{name}</button>\n'

    # Puppy Cards Grid HTML
    puppy_cards = ""
    for idx, pup in enumerate(all_puppies):
        pup_name, pup_gender = clean_pup_record(pup, idx)
        gender_class = pup_gender.lower()
        puppy_cards += f"""
        <div class="puppy-card" data-breed="{pup['breed_slug']}" data-gender="{gender_class}">
            <div class="puppy-img-wrap">
                <img src="{pup['src']}" alt="{pup['alt']}" class="puppy-img" loading="lazy">
            </div>
            <div class="puppy-info">
                <div class="puppy-card-details">
                    <div class="puppy-detail-item">
                        <span class="puppy-detail-label">Name</span>
                        <span style="font-weight: 700;">{pup_name}</span>
                    </div>
                    <div class="puppy-detail-item">
                        <span class="puppy-detail-label">Breed</span>
                        <span style="font-weight: 600;">{pup['breed_name']}</span>
                    </div>
                    <div class="puppy-detail-item">
                        <span class="puppy-detail-label">Gender</span>
                        <span>{pup_gender}</span>
                    </div>
                    <div class="puppy-detail-item">
                        <span class="puppy-detail-label">Status</span>
                        <span class="puppy-status-available" style="color: #339e45; font-weight: 700;">Available</span>
                    </div>
                    <div class="puppy-detail-item">
                        <span class="puppy-detail-label">Delivery</span>
                        <span>Nationwide</span>
                    </div>
                    <div class="puppy-detail-item">
                        <span class="puppy-detail-label">Health</span>
                        <span>Vet Checked</span>
                    </div>
                    <div class="puppy-detail-item">
                        <span class="puppy-detail-label">Vaccinations</span>
                        <span>Up to Date</span>
                    </div>
                    <div class="puppy-detail-item">
                        <span class="puppy-detail-label">Registration</span>
                        <span>Documents Included</span>
                    </div>
                </div>
                <a href="contact-us.html" class="puppy-inquiry-btn">
                    Buy me
                </a>
            </div>
        </div>
        """

    body_content = f"""
    <!-- Available Puppies Header -->
    <section class="section-padding" style="background-color: var(--color-bg-card); padding-bottom: 2rem;">
        <div class="container" style="text-align: center;">
            <h1 class="section-title">Available Puppies for Adoption</h1>
            <p class="section-subtitle" style="max-width: 600px; margin: 0 auto;">Browse all of our current litters. Filter by breed or gender to find your perfect new family member.</p>
        </div>
    </section>

    <!-- Filters and Grid -->
    <section class="section-padding" style="background-color: var(--color-white);">
        <div class="container">
            <div class="filter-section">
                <!-- Breed Buttons -->
                <div class="breed-filters-wrap">
                    {breed_buttons}
                </div>
                <!-- Gender Buttons -->
                <div class="gender-filters">
                    <button class="filter-btn active" data-gender="all">All Genders</button>
                    <button class="filter-btn" data-gender="male">Males Only</button>
                    <button class="filter-btn" data-gender="female">Females Only</button>
                </div>
            </div>

            <!-- Grid -->
            <div class="featured-puppies-grid puppies-grid">
                {puppy_cards}
            </div>
        </div>
    </section>
    """
    
    html = get_head("Available Puppies") + get_header("puppies") + body_content + get_footer()
    with open(os.path.join(DIST_DIR, "available-puppies.html"), "w", encoding="utf-8") as f:
        f.write(html)

def build_kittens_page():
    # Gather only kittens from cat breeds
    all_kittens = []
    for slug in CAT_BREEDS:
        data = puppies_db.get(slug, {})
        for kit in data.get("puppies", []):
            all_kittens.append({
                "breed_slug": slug,
                "breed_name": data["breed_name"],
                "name": kit["name"],
                "alt": kit["alt"],
                "src": kit["src"],
                "gender": kit["gender"]
            })

    # Breed filter buttons HTML
    breed_buttons = '<button class="filter-btn active" data-breed="all">All Breeds</button>\n'
    for slug in CAT_BREEDS:
        name = get_breed_name(slug)
        breed_buttons += f'<button class="filter-btn" data-breed="{slug}">{name}</button>\n'

    # Kitten Cards Grid HTML
    kitten_cards = ""
    for idx, kit in enumerate(all_kittens):
        kit_name, kit_gender = clean_pup_record(kit, idx)
        gender_class = kit_gender.lower()
        kitten_cards += f"""
        <div class="puppy-card" data-breed="{kit['breed_slug']}" data-gender="{gender_class}">
            <div class="puppy-img-wrap">
                <img src="{kit['src']}" alt="{kit['alt']}" class="puppy-img" loading="lazy">
            </div>
            <div class="puppy-info">
                <div class="puppy-card-details">
                    <div class="puppy-detail-item">
                        <span class="puppy-detail-label">Name</span>
                        <span style="font-weight: 700;">{kit_name}</span>
                    </div>
                    <div class="puppy-detail-item">
                        <span class="puppy-detail-label">Breed</span>
                        <span style="font-weight: 600;">{kit['breed_name']}</span>
                    </div>
                    <div class="puppy-detail-item">
                        <span class="puppy-detail-label">Gender</span>
                        <span>{kit_gender}</span>
                    </div>
                    <div class="puppy-detail-item">
                        <span class="puppy-detail-label">Status</span>
                        <span class="puppy-status-available" style="color: #339e45; font-weight: 700;">Available</span>
                    </div>
                    <div class="puppy-detail-item">
                        <span class="puppy-detail-label">Delivery</span>
                        <span>Nationwide</span>
                    </div>
                    <div class="puppy-detail-item">
                        <span class="puppy-detail-label">Health</span>
                        <span>Vet Checked</span>
                    </div>
                    <div class="puppy-detail-item">
                        <span class="puppy-detail-label">Vaccinations</span>
                        <span>Up to Date</span>
                    </div>
                    <div class="puppy-detail-item">
                        <span class="puppy-detail-label">Registration</span>
                        <span>Documents Included</span>
                    </div>
                </div>
                <a href="contact-us.html" class="puppy-inquiry-btn">
                    Buy me
                </a>
            </div>
        </div>
        """

    body_content = f"""
    <!-- Available Kittens Header -->
    <section class="section-padding" style="background-color: var(--color-bg-card); padding-bottom: 2rem;">
        <div class="container" style="text-align: center;">
            <h1 class="section-title">Available Kittens for Adoption</h1>
            <p class="section-subtitle" style="max-width: 600px; margin: 0 auto;">Browse all of our current litters. Filter by breed or gender to find your perfect new family member.</p>
        </div>
    </section>

    <!-- Filters and Grid -->
    <section class="section-padding" style="background-color: var(--color-white);">
        <div class="container">
            <div class="filter-section">
                <!-- Breed Buttons -->
                <div class="breed-filters-wrap">
                    {breed_buttons}
                </div>
                <!-- Gender Buttons -->
                <div class="gender-filters">
                    <button class="filter-btn active" data-gender="all">All Genders</button>
                    <button class="filter-btn" data-gender="male">Males Only</button>
                    <button class="filter-btn" data-gender="female">Females Only</button>
                </div>
            </div>

            <!-- Grid -->
            <div class="featured-puppies-grid puppies-grid">
                {kitten_cards}
            </div>
        </div>
    </section>
    """
    
    html = get_head("Available Kittens") + get_header("kittens") + body_content + get_footer()
    with open(os.path.join(DIST_DIR, "available-kittens.html"), "w", encoding="utf-8") as f:
        f.write(html)

# 7. Build Reviews Page (reviews.html)
def build_reviews_page():
    reviews_cards = ""
    for rev in MOCK_REVIEWS:
        reviews_cards += f"""
        <div class="review-card">
            <div class="review-stars">{'★'*rev['stars']}{'☆'*(5-rev['stars'])}</div>
            <p class="review-quote">"{rev['quote']}"</p>
            <div class="review-author">
                <span>— {rev['author']}</span>
                <span style="font-weight: normal; font-size: 0.8rem; color: var(--color-accent);">{rev['breed']} Owner</span>
            </div>
        </div>
        """

    body_content = f"""
    <!-- Reviews Header -->
    <section class="section-padding" style="background-color: var(--color-bg-card);">
        <div class="container" style="text-align: center;">
            <h1 class="section-title">Pawsome Reviews!</h1>
            <p class="section-subtitle">See what our happy families say about their experiences adopting from Elite Paws.</p>
        </div>
    </section>

    <!-- Reviews Content Grid -->
    <section class="section-padding" style="background-color: var(--color-white);">
        <div class="container">
            <div class="reviews-grid">
                {reviews_cards}
            </div>

            <!-- Submit Review Form -->
            <div class="review-form-container">
                <h3 style="font-family: var(--font-headings); font-size: 1.5rem; margin-bottom: var(--spacing-md); text-align: center;">Leave a Review</h3>
                <form id="review-form">
                    <div class="form-group">
                        <label class="form-label" for="rev-author">Your Name</label>
                        <input class="form-control" type="text" id="rev-author" required placeholder="e.g. John Doe">
                    </div>
                    <div class="form-group">
                        <label class="form-label" for="rev-breed">Puppy's Breed</label>
                        <input class="form-control" type="text" id="rev-breed" required placeholder="e.g. Yorkie">
                    </div>
                    <div class="form-group">
                        <label class="form-label" for="rev-rating">Rating</label>
                        <select class="form-control" id="rev-rating" required>
                            <option value="5">★★★★★ (5 Stars)</option>
                            <option value="4">★★★★☆ (4 Stars)</option>
                            <option value="3">★★★☆☆ (3 Stars)</option>
                            <option value="2">★★☆☆☆ (2 Stars)</option>
                            <option value="1">★☆☆☆☆ (1 Star)</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label class="form-label" for="rev-text">Review Content</label>
                        <textarea class="form-control" id="rev-text" required placeholder="Tell others about your puppy and experience..."></textarea>
                    </div>
                    <button class="btn-submit" type="submit">Submit Review</button>
                </form>
            </div>
        </div>
    </section>
    """
    
    html = get_head("Reviews") + get_header("reviews") + body_content + get_footer()
    with open(os.path.join(DIST_DIR, "reviews.html"), "w", encoding="utf-8") as f:
        f.write(html)

# 8. Build Contact Page (contact-us.html)
def build_contact_page():
    body_content = f"""
    <!-- Contact Us Section -->
    <section class="section-padding" style="background-color: var(--color-bg-main); color: var(--color-headings); padding: 6rem 0; font-family: var(--font-body);">
        <div class="container">
            <!-- Centered Header with Lines -->
            <div style="display: flex; align-items: center; justify-content: center; margin-bottom: 5rem;">
                <div style="flex-grow: 1; height: 1px; background-color: var(--color-border); max-width: 35%;"></div>
                <h1 style="font-family: var(--font-headings); font-size: 2.5rem; font-weight: normal; margin: 0 2rem; color: var(--color-headings); white-space: nowrap; letter-spacing: 1px;">Contact Us</h1>
                <div style="flex-grow: 1; height: 1px; background-color: var(--color-border); max-width: 35%;"></div>
            </div>

            <div class="contact-grid" style="display: grid; grid-template-columns: 1fr 1.1fr; gap: 5rem; align-items: start;">
                
                <!-- Left Column (WhatsApp Info) -->
                <div style="display: flex; flex-direction: column; align-items: flex-start; gap: 20px;">
                    <h2 style="font-family: var(--font-headings); font-size: 2rem; font-weight: normal; color: var(--color-headings); margin: 0 0 10px 0; line-height: 1.3;">Better yet, see us in person!</h2>
                    <p style="color: var(--color-text-main); font-size: 1rem; margin-bottom: 25px; line-height: 1.6; max-width: 480px;">
                        We love our customers, so feel free to visit during normal business hours.
                    </p>
                    
                    <a href="https://wa.me/27715371454" target="_blank" style="background-color: #FFFFFF; color: #1F2937; border-radius: 50px; padding: 12px 28px; font-weight: 700; font-size: 0.95rem; display: inline-flex; align-items: center; gap: 10px; text-decoration: none; transition: transform 0.2s, box-shadow 0.2s; border: 1px solid rgba(0,0,0,0.1); box-shadow: 0 4px 15px rgba(0,0,0,0.06); margin-bottom: 40px;" onmouseover="this.style.transform='translateY(-2px)'" onmouseout="this.style.transform='translateY(0)'">
                        <!-- Green WhatsApp Icon -->
                        <svg style="width: 20px; height: 20px; fill: #25D366; flex-shrink: 0;" viewBox="0 0 448 512">
                            <path d="M380.9 97.1C339 55.1 283.2 32 223.9 32c-122.4 0-222 99.6-222 222 0 39.1 10.2 77.3 29.6 111L3 496l133.9-35.1c32.7 17.9 69.6 27.3 107.1 27.3 122.4 0 222-99.6 222-222 0-59.3-23.2-115-65.1-157.1zM223.9 448c-33.2 0-65.7-8.9-94-25.7l-6.7-4-79.8 20.9 21.3-77.8-4.4-7c-18.5-29.4-28.2-63.3-28.2-98.2 0-101.7 82.8-184.5 184.6-184.5 49.3 0 95.6 19.2 130.4 54.1 34.8 34.9 54 81.2 54 130.4 0 101.7-82.8 184.5-184.6 184.5zm100.5-137.5c-5.5-2.7-32.6-16.1-37.7-17.9-5.1-1.8-8.8-2.7-12.5 2.7-3.7 5.5-14.3 17.9-17.6 21.5-3.3 3.7-6.6 4.1-12.1 1.4-5.5-2.7-23.2-8.5-44.2-27.1-16.4-14.6-27.4-32.7-30.6-38.2-3.3-5.5-.3-8.5 2.4-11.2 2.5-2.4 5.5-6.4 8.2-9.6 2.7-3.3 3.7-5.5 5.5-9.1 1.8-3.7.9-6.9-.5-9.6-1.4-2.7-12.5-30.1-17.1-41.2-4.5-10.8-9.1-9.3-12.5-9.5-3.2-.2-6.9-.2-10.6-.2-3.7 0-9.7 1.4-14.8 6.9-5.1 5.5-19.4 19-19.4 46.3 0 27.3 19.9 53.7 22.6 57.4 2.8 3.7 39.1 59.7 94.8 83.8 13.3 5.7 23.6 9.2 31.6 11.7 13.3 4.2 25.4 3.6 35 2.2 10.7-1.6 32.6-13.3 37.2-26.2 4.6-12.9 4.6-24 3.2-26.2-1.3-2.2-5-3.5-10.5-6.2z"/>
                        </svg>
                        Message us on WhatsApp
                    </a>
                    
                    <div style="font-family: var(--font-headings); font-size: 1.6rem; font-weight: normal; color: var(--color-headings); letter-spacing: 0.5px;">Heavenly Paws Place</div>
                </div>

                <!-- Right Column (Contact Form) -->
                <div style="display: flex; flex-direction: column; gap: 20px; width: 100%;">
                    <h2 style="font-family: var(--font-headings); font-size: 2rem; font-weight: normal; color: var(--color-headings); margin: 0 0 10px 0; line-height: 1.3;">Drop us a line!</h2>
                    
                    <form id="contact-form" style="display: flex; flex-direction: column; gap: 15px; width: 100%;">
                        <!-- Form Inputs Outline Design -->
                        <div style="display: flex; flex-direction: column; gap: 16px;">
                            <input type="text" id="form-name" required placeholder="Name" 
                                style="width: 100%; padding: 14px 18px; background-color: var(--color-white); border: 1px solid var(--color-border); border-radius: 6px; color: var(--color-headings); font-size: 1rem; font-family: var(--font-body); outline: none; transition: border-color 0.2s;"
                                onfocus="this.style.borderColor='var(--color-primary)'" onblur="this.style.borderColor='var(--color-border)'">
                            
                            <input type="email" id="form-email" required placeholder="Email*" 
                                style="width: 100%; padding: 14px 18px; background-color: var(--color-white); border: 1px solid var(--color-border); border-radius: 6px; color: var(--color-headings); font-size: 1rem; font-family: var(--font-body); outline: none; transition: border-color 0.2s;"
                                onfocus="this.style.borderColor='var(--color-primary)'" onblur="this.style.borderColor='var(--color-border)'">
                            
                            <input type="tel" id="form-whatsapp" required placeholder="WhatsApp Only*" 
                                style="width: 100%; padding: 14px 18px; background-color: var(--color-white); border: 1px solid var(--color-border); border-radius: 6px; color: var(--color-headings); font-size: 1rem; font-family: var(--font-body); outline: none; transition: border-color 0.2s;"
                                onfocus="this.style.borderColor='var(--color-primary)'" onblur="this.style.borderColor='var(--color-border)'">
                            
                            <input type="text" id="form-puppy" required placeholder="Interested Puppy's Name*" 
                                style="width: 100%; padding: 14px 18px; background-color: var(--color-white); border: 1px solid var(--color-border); border-radius: 6px; color: var(--color-headings); font-size: 1rem; font-family: var(--font-body); outline: none; transition: border-color 0.2s;"
                                onfocus="this.style.borderColor='var(--color-primary)'" onblur="this.style.borderColor='var(--color-border)'">
                            
                            <input type="text" id="form-breed" placeholder="Interested Puppy's Breed" 
                                style="width: 100%; padding: 14px 18px; background-color: var(--color-white); border: 1px solid var(--color-border); border-radius: 6px; color: var(--color-headings); font-size: 1rem; font-family: var(--font-body); outline: none; transition: border-color 0.2s;"
                                onfocus="this.style.borderColor='var(--color-primary)'" onblur="this.style.borderColor='var(--color-border)'">
                            
                            <input type="text" id="form-province" required placeholder="Province*" 
                                style="width: 100%; padding: 14px 18px; background-color: var(--color-white); border: 1px solid var(--color-border); border-radius: 6px; color: var(--color-headings); font-size: 1rem; font-family: var(--font-body); outline: none; transition: border-color 0.2s;"
                                onfocus="this.style.borderColor='var(--color-primary)'" onblur="this.style.borderColor='var(--color-border)'">
                            
                            <textarea id="form-msg" required placeholder="Message*" rows="5"
                                style="width: 100%; padding: 14px 18px; background-color: var(--color-white); border: 1px solid var(--color-border); border-radius: 6px; color: var(--color-headings); font-size: 1rem; font-family: var(--font-body); outline: none; resize: vertical; transition: border-color 0.2s;"
                                onfocus="this.style.borderColor='var(--color-primary)'" onblur="this.style.borderColor='var(--color-border)'"></textarea>
                        </div>

                        <!-- Rounded Grey Pill Send Button -->
                        <button type="submit" class="contact-send-btn" 
                            style="width: 100%; background-color: #6B7280; color: #FFFFFF; border: none; border-radius: 50px; padding: 14px 28px; font-weight: 600; font-size: 1.05rem; cursor: pointer; transition: background-color 0.2s, transform 0.1s;"
                            onmouseover="this.style.backgroundColor='#4B5563'" onmouseout="this.style.backgroundColor='#6B7280'"
                            onmousedown="this.style.transform='scale(0.98)'" onmouseup="this.style.transform='scale(1)'">
                            Send
                        </button>
                        
                        <!-- Footnote -->
                        <p style="font-size: 0.75rem; color: var(--color-text-light); text-align: center; margin-top: 15px; line-height: 1.4; font-family: var(--font-body);">
                            This site is protected by reCAPTCHA and the Google <a href="https://policies.google.com/privacy" target="_blank" style="color: var(--color-text-light); text-decoration: underline;">Privacy Policy</a> and <a href="https://policies.google.com/terms" target="_blank" style="color: var(--color-text-light); text-decoration: underline;">Terms of Service</a> apply.
                        </p>
                    </form>
                </div>

            </div>
        </div>
    </section>
    """
    
    html = get_head("Contact Us") + get_header("contact") + body_content + get_footer()
    with open(os.path.join(DIST_DIR, "contact-us.html"), "w", encoding="utf-8") as f:
        f.write(html)

# 9. Build Breed Pages (yorkie.html, rottweiler.html, etc.)
def build_breed_pages():
    for slug in BREED_SLUGS:
        data = puppies_db.get(slug, {
            "breed_name": slug.replace("-", " ").title(),
            "puppies": [],
            "texts": ["Parents: Healthy and Vaccinated", "Registration Documents Included"]
        })
        
        breed_name = data["breed_name"]
        puppies = data.get("puppies", [])
        bullets = data.get("texts", ["Parents: Healthy and Vaccinated", "Registration Documents Included"])
        
        is_cat = slug in CAT_BREEDS
        type_noun = "Kittens" if is_cat else "Puppies"
        type_singular = "kitten" if is_cat else "puppy"

        # Build bullet list HTML
        bullet_items = ""
        for b in bullets:
            bullet_items += f'<li style="margin-bottom: 8px; list-style-type: disc; margin-left: 20px; font-weight: 700; color: var(--color-primary-dark);">{b}</li>\n'
            
        # Build puppies grid HTML
        puppy_cards = ""
        if puppies:
            for idx, pup in enumerate(puppies):
                pup_name, pup_gender = clean_pup_record(pup, idx)
                gender_class = pup_gender.lower()
                puppy_cards += f"""
                <div class="puppy-card" data-breed="{slug}" data-gender="{gender_class}">
                    <div class="puppy-img-wrap">
                        <img src="{pup['src']}" alt="{pup['alt']}" class="puppy-img" loading="lazy">
                    </div>
                    <div class="puppy-info">
                        <div class="puppy-card-details">
                            <div class="puppy-detail-item">
                                <span class="puppy-detail-label">Name</span>
                                <span style="font-weight: 700;">{pup_name}</span>
                            </div>
                            <div class="puppy-detail-item">
                                <span class="puppy-detail-label">Breed</span>
                                <span style="font-weight: 600;">{breed_name}</span>
                            </div>
                            <div class="puppy-detail-item">
                                <span class="puppy-detail-label">Gender</span>
                                <span>{pup_gender}</span>
                            </div>
                            <div class="puppy-detail-item">
                                <span class="puppy-detail-label">Status</span>
                                <span class="puppy-status-available" style="color: #339e45; font-weight: 700;">Available</span>
                            </div>
                            <div class="puppy-detail-item">
                                <span class="puppy-detail-label">Delivery</span>
                                <span>Nationwide</span>
                            </div>
                            <div class="puppy-detail-item">
                                <span class="puppy-detail-label">Health</span>
                                <span>Vet Checked</span>
                            </div>
                            <div class="puppy-detail-item">
                                <span class="puppy-detail-label">Vaccinations</span>
                                <span>Up to Date</span>
                            </div>
                            <div class="puppy-detail-item">
                                <span class="puppy-detail-label">Registration</span>
                                <span>Documents Included</span>
                            </div>
                        </div>
                        <a href="contact-us.html" class="puppy-inquiry-btn">
                            Buy me
                        </a>
                    </div>
                </div>
                """
        else:
            puppy_cards = f"""
            <div style="grid-column: 1 / -1; text-align: center; padding: 4rem 1rem; background-color: var(--color-bg-card); border-radius: var(--radius-card); border: 1px solid var(--color-border);">
                <h3 style="font-family: var(--font-headings); font-size: 1.5rem; margin-bottom: var(--spacing-sm);">No {type_singular}s currently available</h3>
                <p style="color: var(--color-text-light); margin-bottom: var(--spacing-md); max-width: 500px; margin-left: auto; margin-right: auto;">
                    We don't currently have any active {breed_name} litters ready for adoption. Join our waiting list on WhatsApp to get notified as soon as our next litter is born!
                </p>
                <a href="https://wa.me/27715371454?text=Hi!%20I%20want%20to%20join%20the%20waiting%20list%20for%20{breed_name}%20{type_singular}s." target="_blank" class="btn-primary">
                    Join waiting list
                </a>
            </div>
            """

        body_content = f"""
        <!-- Breed Page Header -->
        <section class="section-padding" style="background-color: var(--color-bg-card);">
            <div class="container" style="display: grid; grid-template-columns: 1.2fr 0.8fr; gap: var(--spacing-xl); align-items: center;">
                <div>
                    <h1 class="section-title" style="font-size: 2.75rem; margin-bottom: var(--spacing-sm);">{breed_name}</h1>
                    <p class="section-subtitle" style="margin-bottom: var(--spacing-md);">Adopt a healthy, registered, and socialized {breed_name} {type_singular} from our loving home.</p>
                    <ul style="margin-bottom: var(--spacing-md);">
                        {bullet_items}
                    </ul>
                    <a href="https://wa.me/27715371454?text=Hi!%20I%20have%20an%20inquiry%20about%20your%20{breed_name}%20{type_singular}s." target="_blank" class="nav-whatsapp-btn" style="padding: 12px 28px;">
                        Inquire on WhatsApp
                    </a>
                </div>
                <div style="text-align: center;">
                    <img src="{LOGO_IMG}" alt="Breed logo" style="max-width: 220px; border-radius: 50%; border: 4px solid var(--color-white); box-shadow: var(--shadow-medium); margin: 0 auto;">
                </div>
            </div>
        </section>

        <!-- Puppies Grid -->
        <section class="section-padding" style="background-color: var(--color-white);">
            <div class="container">
                <h2 style="font-family: var(--font-headings); font-size: 1.75rem; margin-bottom: var(--spacing-lg); border-bottom: 2px solid var(--color-bg-card); padding-bottom: 10px;">
                    Available {breed_name} {type_noun}
                </h2>
                <div class="featured-puppies-grid puppies-grid">
                    {puppy_cards}
                </div>
            </div>
        </section>
        """
        
        html = get_head(f"{breed_name} {type_noun}") + get_header("breeds") + body_content + get_footer()
        with open(os.path.join(DIST_DIR, f"{slug}.html"), "w", encoding="utf-8") as f:
            f.write(html)
            
    print(f"Generated {len(BREED_SLUGS)} breed-specific pages.")

# 10. Run Builder
if __name__ == "__main__":
    print("Compiling website...")
    build_homepage()
    print("  Homepage index.html generated.")
    build_puppies_page()
    print("  Puppies Directory available-puppies.html generated.")
    build_kittens_page()
    print("  Kittens Directory available-kittens.html generated.")
    build_reviews_page()
    print("  Reviews reviews.html generated.")
    build_contact_page()
    print("  Contact contact-us.html generated.")
    # build_breed_pages()
    print("Compilation successful! Output files in dist/ directory.")
