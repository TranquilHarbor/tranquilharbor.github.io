# TranquilHarbor - NICE CXone Demo Site

A demo medical website designed specifically for testing and showcasing NICE CXone products and integrations. This project provides a realistic environment for evaluating CXone's customer experience solutions in a healthcare context.

## NICE CXone Integration

This site demonstrates several CXone capabilities:
- Customer chat integration
- Guide functionality
- Custom translations
- Customizable UI elements
- Pre-survey options
- Entry point configuration

The CXone configuration can be found in the script section of the HTML files, where various features can be enabled, disabled, or customized.

## Technologies Used

- Python 3 / Flask (web application)
- HTML5 / Jinja2 templates
- CSS3
- JavaScript
- Bootstrap
- jQuery
- Font Awesome
- Owl Carousel
- WOW.js for animations
- NICE CXone for customer interaction

## Features

- Responsive design that works on all devices
- Modern and clean user interface
- Interactive carousel/slider
- Smooth scrolling navigation
- Animated elements
- Customer chat integration
- Special offers section
- News/blog section
- Team showcase
- Appointment booking form

## Project Structure

**Flask app structure:**
```
├── app.py             # Flask application and routes
├── requirements.txt   # Python dependencies
├── static/            # CSS, JS, images, fonts (served by Flask)
│   ├── css/
│   ├── js/
│   ├── images/
│   └── fonts/
└── templates/         # Jinja2 templates
    ├── base.html
    ├── index.html
    ├── news_detail.html
    └── special_offer.html
```

## Pages / Routes

| Route | Description |
|-------|-------------|
| `/` | Main homepage |
| `/news-detail/` | News article details |
| `/special-offer/` | Special offers page |

## Setup

**Run as Flask app (recommended):**
```bash
pip install -r requirements.txt
flask run
```
Then open http://127.0.0.1:5000/


## License

See the [LICENSE](LICENSE) file for details.

---
Last updated: October 16, 2025