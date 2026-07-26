/* -------------------------------------------------------------
   ElitePawsworld - Interactive Logic & Client-side Router/Filter
------------------------------------------------------------- */

document.addEventListener('DOMContentLoaded', () => {
    // 1. Header Scrolled State
    const header = document.querySelector('.site-header');
    if (header) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 20) {
                header.classList.add('scrolled');
            } else {
                header.classList.remove('scrolled');
            }
        });
    }

    // 1.5 Hero Background Slideshow
    const slides = document.querySelectorAll('.hero-bg-img');
    const indicators = document.querySelectorAll('.hero-indicators .indicator');
    if (slides.length && indicators.length) {
        let currentSlide = 0;
        let slideInterval;
        const intervalTime = 5000; // 5 seconds per slide

        const showSlide = (n) => {
            slides.forEach(slide => slide.classList.remove('active'));
            indicators.forEach(ind => ind.classList.remove('active'));
            currentSlide = (n + slides.length) % slides.length;
            slides[currentSlide].classList.add('active');
            indicators[currentSlide].classList.add('active');
        };

        const nextSlide = () => {
            showSlide(currentSlide + 1);
        };

        const startInterval = () => {
            clearInterval(slideInterval);
            slideInterval = setInterval(nextSlide, intervalTime);
        };

        indicators.forEach((indicator, index) => {
            indicator.addEventListener('click', () => {
                showSlide(index);
                startInterval();
            });
        });

        startInterval();
    }

    // 2. Mobile Menu Toggle
    const hamburger = document.querySelector('.hamburger');
    const navMenu = document.querySelector('.nav-menu');
    if (hamburger && navMenu) {
        hamburger.addEventListener('click', () => {
            hamburger.classList.toggle('open');
            navMenu.classList.toggle('open');
            // Prevent body scroll when menu is open
            document.body.classList.toggle('disable-scroll');
        });

        // Close menu when clicking links
        const navLinks = document.querySelectorAll('.nav-link, .dropdown-link');
        navLinks.forEach(link => {
            link.addEventListener('click', () => {
                hamburger.classList.remove('open');
                navMenu.classList.remove('open');
                document.body.classList.remove('disable-scroll');
            });
        });
    }

    // 3. Persistent Cookie Banner
    const cookieBanner = document.querySelector('.cookie-banner');
    const acceptBtn = document.querySelector('.cookie-accept-btn');
    if (cookieBanner && acceptBtn) {
        // Check if user already accepted
        if (localStorage.getItem('cookie_accepted') === 'true') {
            cookieBanner.classList.add('hidden');
        }

        acceptBtn.addEventListener('click', (e) => {
            e.preventDefault();
            localStorage.setItem('cookie_accepted', 'true');
            cookieBanner.classList.add('hidden');
        });
    }

    // 4. Puppies Grid Filtering Logic (only runs on available-puppies.html or breed-specific pages if they use the grid)
    const puppiesGrid = document.querySelector('.puppies-grid');
    if (puppiesGrid) {
        const breedButtons = document.querySelectorAll('.breed-filters-wrap .filter-btn');
        const genderButtons = document.querySelectorAll('.gender-filters .filter-btn');
        const puppyCards = document.querySelectorAll('.puppy-card');

        let activeBreed = 'all';
        let activeGender = 'all';

        // Check URL Query Parameter (e.g. ?breed=yorkie)
        const urlParams = new URLSearchParams(window.location.search);
        const breedParam = urlParams.get('breed');
        if (breedParam) {
            activeBreed = breedParam;
            // Highlight the correct filter button
            breedButtons.forEach(btn => {
                if (btn.dataset.breed === breedParam) {
                    btn.classList.add('active');
                } else {
                    btn.classList.remove('active');
                }
            });
        }

        // Apply filters function
        function applyFilters() {
            let visibleCount = 0;
            puppyCards.forEach(card => {
                const cardBreed = card.dataset.breed;
                const cardGender = card.dataset.gender;

                const matchesBreed = (activeBreed === 'all' || cardBreed === activeBreed);
                const matchesGender = (activeGender === 'all' || cardGender === activeGender);

                if (matchesBreed && matchesGender) {
                    card.style.display = 'flex';
                    // Trigger reflow for transition effect
                    card.style.opacity = '0';
                    card.style.transform = 'scale(0.95)';
                    setTimeout(() => {
                        card.style.opacity = '1';
                        card.style.transform = 'scale(1)';
                        card.style.transition = 'opacity 0.4s ease, transform 0.4s ease';
                    }, 50);
                    visibleCount++;
                } else {
                    card.style.display = 'none';
                }
            });

            // Handle empty search results state
            let noResultsMsg = document.getElementById('no-puppies-msg');
            if (visibleCount === 0) {
                if (!noResultsMsg) {
                    noResultsMsg = document.createElement('div');
                    noResultsMsg.id = 'no-puppies-msg';
                    noResultsMsg.style.textAlign = 'center';
                    noResultsMsg.style.gridColumn = '1 / -1';
                    noResultsMsg.style.padding = '3rem';
                    noResultsMsg.style.color = 'var(--color-text-light)';
                    noResultsMsg.innerHTML = `
                        <h3 style="margin-bottom: 10px;">No Puppies Available</h3>
                        <p>We don't currently have any puppies listed matching these filters. Please select another breed or contact us directly!</p>
                    `;
                    puppiesGrid.appendChild(noResultsMsg);
                } else {
                    noResultsMsg.style.display = 'block';
                }
            } else if (noResultsMsg) {
                noResultsMsg.style.display = 'none';
            }
        }

        // Bind breed filter buttons
        breedButtons.forEach(btn => {
            btn.addEventListener('click', () => {
                breedButtons.forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                activeBreed = btn.dataset.breed;
                
                // Update URL parameter without page reload
                const newUrl = new URL(window.location.href);
                if (activeBreed === 'all') {
                    newUrl.searchParams.delete('breed');
                } else {
                    newUrl.searchParams.set('breed', activeBreed);
                }
                window.history.pushState({}, '', newUrl);

                applyFilters();
            });
        });

        // Bind gender filter buttons
        genderButtons.forEach(btn => {
            btn.addEventListener('click', () => {
                genderButtons.forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                activeGender = btn.dataset.gender;
                applyFilters();
            });
        });

        // Initial Filter Application
        applyFilters();
    }

    // 5. Contact Form Handler
    const contactForm = document.getElementById('contact-form');
    if (contactForm) {
        contactForm.addEventListener('submit', (e) => {
            e.preventDefault();
            // Get form inputs
            const name = document.getElementById('form-name').value;
            const email = document.getElementById('form-email').value;
            const breed = document.getElementById('form-breed').value;
            const puppy = document.getElementById('form-puppy').value;

            // Success feedback
            const container = contactForm.parentElement;
            container.innerHTML = `
                <div class="success-message" style="text-align: center; padding: var(--spacing-lg) 0; animation: fadeInUp 0.5s ease;">
                    <div style="font-size: 3.5rem; color: var(--color-success); margin-bottom: var(--spacing-sm);">✓</div>
                    <h3 style="margin-bottom: var(--spacing-sm);">Thank you, ${name}!</h3>
                    <p style="color: var(--color-text-light); margin-bottom: var(--spacing-md);">Your message and inquiry for the ${breed} puppy (${puppy || 'General Inquiry'}) has been sent. We'll get back to you shortly via Email or WhatsApp.</p>
                    <a href="available-puppies.html" class="btn-primary" style="padding: 10px 24px; font-size: 0.9rem;">Back to Puppies</a>
                </div>
            `;
        });
    }

    // 6. Review Form Handler
    const reviewForm = document.getElementById('review-form');
    if (reviewForm) {
        reviewForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const author = document.getElementById('rev-author').value;
            const breed = document.getElementById('rev-breed').value;
            const reviewText = document.getElementById('rev-text').value;
            const stars = document.getElementById('rev-rating').value;

            // Prepend new review card to reviews-grid
            const reviewsGrid = document.querySelector('.reviews-grid');
            if (reviewsGrid) {
                const newCard = document.createElement('div');
                newCard.className = 'review-card';
                newCard.style.animation = 'fadeInUp 0.6s ease';
                newCard.innerHTML = `
                    <div class="review-stars">${'★'.repeat(stars)}${'☆'.repeat(5-stars)}</div>
                    <p class="review-quote">"${reviewText}"</p>
                    <div class="review-author">
                        <span>— ${author}</span>
                        <span style="font-weight: normal; font-size: 0.8rem; color: var(--color-accent);">${breed} Owner</span>
                    </div>
                `;
                reviewsGrid.insertBefore(newCard, reviewsGrid.firstChild);
                
                // Clear form & alert success
                reviewForm.reset();
                alert('Thank you for sharing your pawsome review! It has been posted.');
            }
        });
    }

    // 7. Testimonials Slider Arrows
    const sliderWrap = document.getElementById('home-reviews-slider-wrap');
    const prevBtn = document.getElementById('reviews-prev-btn');
    const nextBtn = document.getElementById('reviews-next-btn');
    if (sliderWrap && prevBtn && nextBtn) {
        prevBtn.addEventListener('click', () => {
            sliderWrap.scrollBy({ left: -440, behavior: 'smooth' });
        });
        nextBtn.addEventListener('click', () => {
            sliderWrap.scrollBy({ left: 440, behavior: 'smooth' });
        });
    }

    // 8. FAQ Accordion Toggle
    const faqItems = document.querySelectorAll('.faq-item');
    faqItems.forEach(item => {
        const question = item.querySelector('.faq-question');
        if (question) {
            question.addEventListener('click', () => {
                faqItems.forEach(otherItem => {
                    if (otherItem !== item) {
                        otherItem.classList.remove('active');
                    }
                });
                item.classList.toggle('active');
            });
        }
    });

    // 9. Intersection Observer for Fade-up Reveal on Scroll
    const revealElements = document.querySelectorAll('.reveal');
    revealElements.forEach(el => el.classList.add('visible'));
    if ('IntersectionObserver' in window && revealElements.length > 0) {
        const observer = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                    observer.unobserve(entry.target);
                }
            });
        }, {
            threshold: 0.05,
            rootMargin: "50px 0px 50px 0px"
        });
        revealElements.forEach(el => observer.observe(el));
    }
    // 10. Contact Form Button Color Change on Input
    const contactForms = document.querySelectorAll('form');
    contactForms.forEach(form => {
        const sendBtn = form.querySelector('.contact-send-btn');
        if (sendBtn) {
            const checkFields = () => {
                const inputs = form.querySelectorAll('input, textarea');
                let hasValue = false;
                inputs.forEach(input => {
                    if (input.value && input.value.trim().length > 0) {
                        hasValue = true;
                    }
                });
                if (hasValue) {
                    sendBtn.classList.add('active');
                    sendBtn.style.backgroundColor = 'var(--color-primary)';
                } else {
                    sendBtn.classList.remove('active');
                    sendBtn.style.backgroundColor = '#6B7280';
                }
            };

            form.addEventListener('input', checkFields);
            form.addEventListener('change', checkFields);
            checkFields();
        }
    });
});
