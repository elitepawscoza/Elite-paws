<?php
header('Content-Type: application/json');

// Recipient email address on cPanel
$to_email = "info@elitepawsworld.co.za"; 

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Sanitize input fields
    $name     = isset($_POST['name'])     ? filter_var(trim($_POST['name']), FILTER_SANITIZE_STRING) : '';
    $email    = isset($_POST['email'])    ? filter_var(trim($_POST['email']), FILTER_VALIDATE_EMAIL) : '';
    $whatsapp = isset($_POST['whatsapp']) ? filter_var(trim($_POST['whatsapp']), FILTER_SANITIZE_STRING) : '';
    $puppy    = isset($_POST['puppy'])    ? filter_var(trim($_POST['puppy']), FILTER_SANITIZE_STRING) : '';
    $breed    = isset($_POST['breed'])    ? filter_var(trim($_POST['breed']), FILTER_SANITIZE_STRING) : '';
    $province = isset($_POST['province']) ? filter_var(trim($_POST['province']), FILTER_SANITIZE_STRING) : '';
    $message  = isset($_POST['message'])  ? filter_var(trim($_POST['message']), FILTER_SANITIZE_STRING) : '';

    if (empty($name) || empty($email) || empty($whatsapp) || empty($message)) {
        http_response_code(400);
        echo json_encode(["status" => "error", "message" => "Please complete all required fields."]);
        exit;
    }

    $subject = "New Puppy Adoption Inquiry from " . $name;

    // Email Body (HTML formatted)
    $email_content = "
    <html>
    <head>
      <title>New Adoption Inquiry - Elite Paws World</title>
      <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; color: #333; }
        .container { max-width: 600px; margin: 0 auto; padding: 20px; border: 1px solid #e0e0e0; border-radius: 8px; }
        h2 { color: #8B5E3C; border-bottom: 2px solid #8B5E3C; padding-bottom: 8px; }
        .field { margin-bottom: 12px; }
        .label { font-weight: bold; color: #555; }
        .value { background: #f9f9f9; padding: 8px 12px; border-radius: 4px; display: block; margin-top: 4px; }
      </style>
    </head>
    <body>
      <div class='container'>
        <h2>🐾 New Puppy Adoption Inquiry</h2>
        <div class='field'><span class='label'>Name:</span> <span class='value'>$name</span></div>
        <div class='field'><span class='label'>Email:</span> <span class='value'>$email</span></div>
        <div class='field'><span class='label'>WhatsApp Number:</span> <span class='value'>$whatsapp</span></div>
        <div class='field'><span class='label'>Interested Puppy:</span> <span class='value'>$puppy</span></div>
        <div class='field'><span class='label'>Interested Breed:</span> <span class='value'>" . ($breed ?: 'Not Specified') . "</span></div>
        <div class='field'><span class='label'>Province:</span> <span class='value'>$province</span></div>
        <div class='field'><span class='label'>Message:</span> <span class='value'>" . nl2br($message) . "</span></div>
      </div>
    </body>
    </html>
    ";

    // Headers
    $headers  = "MIME-Version: 1.0" . "\r\n";
    $headers .= "Content-type:text/html;charset=UTF-8" . "\r\n";
    $headers .= "From: Elite Paws World <no-reply@elitepawsworld.co.za>" . "\r\n";
    $headers .= "Reply-To: $email" . "\r\n";

    if (mail($to_email, $subject, $email_content, $headers)) {
        http_response_code(200);
        echo json_encode(["status" => "success", "message" => "Thank you! Your adoption inquiry has been sent successfully. We will contact you shortly."]);
    } else {
        http_response_code(500);
        echo json_encode(["status" => "error", "message" => "Server error: Unable to send email. Please message us directly on WhatsApp."]);
    }
} else {
    http_response_code(405);
    echo json_encode(["status" => "error", "message" => "Method not allowed."]);
}
?>
