// Theme and Color Contrast Handler

(function() {
  // Color Contrast Utility
  function adjustColorContrast() {
    const root = document.documentElement;
    const isDarkMode = document.body.classList.contains('dark-mode');

    // Define color palettes
    const lightPalette = {
      background: '#ffffff',
      primaryText: '#333333',
      secondaryText: '#666666',
      accent: '#228B22'
    };

    const darkPalette = {
      background: '#121212',
      primaryText: '#e0e0e0',
      secondaryText: '#a0a0a0',
      accent: '#4CAF50'
    };

    // Select current palette based on mode
    const palette = isDarkMode ? darkPalette : lightPalette;

    // Apply color variables
    root.style.setProperty('--background-color', palette.background);
    root.style.setProperty('--primary-text-color', palette.primaryText);
    root.style.setProperty('--secondary-text-color', palette.secondaryText);
    root.style.setProperty('--accent-color', palette.accent);

    // Adjust specific elements
    const elementsToAdjust = [
      '.text-lead', 
      'h1', 'h2', 'h3', 
      'p', 
      '.contact-method', 
      '.availability-card'
    ];

    elementsToAdjust.forEach(selector => {
      const elements = document.querySelectorAll(selector);
      elements.forEach(el => {
        el.style.color = palette.primaryText;
      });
    });
  }

  // Image Reference Handler
  function handleImageReferences() {
    const imageMap = {
      'profile-image': 'https://raw.githubusercontent.com/ssmanji89/jekyll-TeXt-theme.sulemanji.com/master/assets/images/sulemanji-profile.jpg',
      'case-study-cover': 'https://cdn.sulemanji.com/case-studies/cover-placeholder.jpg'
      // Add more image mappings as needed
    };

    Object.keys(imageMap).forEach(key => {
      const elements = document.querySelectorAll(`[data-image-key="${key}"]`);
      elements.forEach(el => {
        el.src = imageMap[key];
        el.setAttribute('alt', `Suleman Manji - ${key}`);
      });
    });
  }

  // Theme Toggle
  function setupThemeToggle() {
    const themeToggle = document.getElementById('theme-toggle');
    if (themeToggle) {
      themeToggle.addEventListener('click', () => {
        document.body.classList.toggle('dark-mode');
        adjustColorContrast();
        handleImageReferences();
        
        // Persist theme preference
        localStorage.setItem('theme-preference', 
          document.body.classList.contains('dark-mode') ? 'dark' : 'light'
        );
      });
    }

    // Restore theme preference
    const savedTheme = localStorage.getItem('theme-preference');
    if (savedTheme === 'dark') {
      document.body.classList.add('dark-mode');
    }
  }

  // Initialize on DOM load
  document.addEventListener('DOMContentLoaded', () => {
    adjustColorContrast();
    handleImageReferences();
    setupThemeToggle();
  });

  // Expose methods for manual trigger
  window.themeHandler = {
    adjustColorContrast,
    handleImageReferences
  };
})();
