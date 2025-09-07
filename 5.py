<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Arsiel Jey Bacatin - Personal Website</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://kit.fontawesome.com/a076d05399.js" crossorigin="anonymous"></script>
    <style>
        /* Custom styles for uniqueness */
        body {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            font-family: 'Roboto', sans-serif;
        }
        .hero-section {
            background: url('https://storage.googleapis.com/workspace-0f70711f-8b4e-4d94-86f1-2a93ccde5887/image/a096b5ca-5afa-4f92-8576-0c9e7d704ab8.png') no-repeat center center/cover;
            background-attachment: fixed;
        }
        .fade-in {
            opacity: 0;
            animation: fadeIn 2s ease-in forwards;
        }
        @keyframes fadeIn {
            to { opacity: 1; }
        }
        .glow {
            text-shadow: 0 0 10px rgba(255, 255, 255, 0.5);
        }
        section {
            padding: 4rem 2rem;
        }
        .btn {
            transition: all 0.3s ease;
        }
        .btn:hover {
            transform: scale(1.05);
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
        }
        .image-container img {
            max-width: 100%;
            height: auto;
            border-radius: 10px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
        }
        .social-links a {
            margin: 0 10px;
            text-decoration: none;
        }
        .social-links i {
            font-size: 2rem;
            color: #333;
            transition: color 0.3s;
        }
        .social-links i:hover {
            color: #667eea;
        }
    </style>
</head>
<body class="text-white">
    <header class="hero-section text-center py-20 fade-in">
        <div class="container mx-auto">
            <h1 class="text-5xl font-bold mb-2">Arsiel Jey Bacatin</h1>
            <p class="text-xl mb-4">a Programmer</p>
            <div class="mb-4">
                <img src="https://storage.googleapis.com/workspace-0f70711f-8b4e-4d94-86f1-2a93ccde5887/image/23d3cbb6-4c05-4dc2-94d8-ae33eaf3beb3.png" alt="Majestic cloud-covered mountain peak with snow and forested base in a serene landscape, evoking freedom and adventure">
            </div>
            <div class="image-container">
                <img src="https://storage.googleapis.com/workspace-0f70711f-8b4e-4d94-86f1-2a93ccde5887/image/299b7672-6d69-4e75-98e5-e8f68af49560.png" alt="Professional portrait of Arsiel Jey Bacatin, a confident programmer with glasses, wearing a casual tech-themed shirt, smiling warmly in a bright studio setting">
            </div>
        </div>
    </header>

    <section class="bg-gray-100 text-gray-800 text-center fade-in">
        <div class="container mx-auto max-w-4xl">
            <h2 class="text-4xl font-bold mb-4">Hello.</h2>
            <p class="text-lg mb-4">I am an iOS and Web Developer. I'm the founder and CTO of The App Brewery. I ❤️ coffee and brew my own beers.</p>
        </div>
    </section>

    <section class="bg-white text-gray-800 fade-in">
        <div class="container mx-auto max-w-4xl">
            <h2 class="text-4xl font-bold mb-4 text-center">My Skills</h2>
            <div class="image-container mb-4">
                <img src="https://storage.googleapis.com/workspace-0f70711f-8b4e-4d94-86f1-2a93ccde5887/image/3590d148-ca49-4787-aae3-691949b92c5e.png" alt="Cute orange tabby cat intently typing on a laptop keyboard, with paws on the keys, looking focused and adorable in a cozy home office">
            </div>
            <h3 class="text-2xl font-semibold mb-2">Design & Development</h3>
            <p class="text-lg">I started learning to code when I was 12 years old because I wanted to make my own video games. Over time, I have gained a wealth of experience designing and developing mobile and web applications.</p>
        </div>
    </section>

    <section class="bg-gray-200 text-gray-800 fade-in">
        <div class="container mx-auto max-w-4xl text-center">
            <h2 class="text-4xl font-bold mb-4">Hot Wings Challenge</h2>
            <div class="image-container mb-4">
                <img src="https://storage.googleapis.com/workspace-0f70711f-8b4e-4d94-86f1-2a93ccde5887/image/0f878af7-ac86-4d59-a063-824977848460.png" alt="Fiery red chillies including ghost peppers and Carolina reapers, arranged artistically on a rustic wooden table with steam rising and a hint of spice in the air">
            </div>
            <p class="text-lg mb-4">But my best skill is actually in eating hot wings. I am the undisputed queen of hot wing challenges. Ghost Peppers and Carolina Reapers are my favourite snacks.</p>
        </div>
    </section>

    <section class="bg-blue-600 text-white text-center fade-in">
        <div class="container mx-auto max-w-4xl">
            <h2 class="text-4xl font-bold mb-4">Get In Touch</h2>
            <p class="text-lg mb-4">If you love hot wings as much as I do. Love hot wings as much as I do? Let's talk about how awesome they are! We can code while we eat hot wings!</p>
            <h3 class="text-2xl font-semibold mb-4">CONTACT ME</h3>
            <div class="social-links">
                <a href="#" aria-label="TikTok"><i class="fab fa-tiktok"></i></a>
                <a href="#" aria-label="YouTube"><i class="fab fa-youtube"></i></a>
                <a href="#" aria-label="Facebook"><i class="fab fa-facebook"></i></a>
                <a href="#" aria-label="Website"><i class="fas fa-globe"></i></a>
            </div>
        </div>
    </section>

    <footer class="bg-gray-800 text-center py-8 fade-in">
        <p class="text-lg">© Arsiel Jey Bacatin @ The App Brewery.<br>Design HTML and JavaScript Brewery.</p>
    </footer>

    <script>
        // Simple JS for animations or interactivity
        window.addEventListener('load', function() {
            const elements = document.querySelectorAll('.fade-in');
            elements.forEach(el => {
                el.classList.add('fade-in-animated');
            });
        });

        // Add a button to scroll to top if needed, but since it's a single page, optional
        // For uniqueness, add a coffee lover's joke on hover or click
        const hero = document.querySelector('.hero-section');
        hero.addEventListener('click', () => {
            alert('Brewing success, one code at a time!');
        });
    </script>
</body>
</html>
</content>
</create_file>
