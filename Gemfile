source 'https://rubygems.org'

# Explicitly set Ruby version compatibility
ruby '~> 3.1.0'

# GitHub Pages (specific version for compatibility)
gem 'github-pages', '~> 232'

# Core Jekyll with compatible version
gem 'jekyll', '3.10.0'

# Theme Management
gem 'jekyll-remote-theme'
gem 'jekyll-text-theme', git: 'https://github.com/kitian616/jekyll-TeXt-theme.git'

# Essential Plugins
group :jekyll_plugins do
  gem 'jekyll-feed', '~> 0.17.0'
  gem 'jekyll-paginate', '~> 1.1.0'
  gem 'jekyll-sitemap', '~> 1.4.0'
  gem 'jekyll-seo-tag', '~> 2.8.0'
  gem 'jekyll-redirect-from', '~> 0.16.0'
  gem 'jemoji', '~> 0.13.0'
  gem 'jekyll-include-cache', '~> 0.2.1'
  
  # Markdown and Syntax Highlighting
  gem 'kramdown', '2.4.0'
  gem 'kramdown-parser-gfm', '~> 1.1.0'
  gem 'rouge', '~> 3.30.0'
end

# Development and Compatibility Gems
group :development do
  gem 'webrick'
  gem 'wdm', '>= 0.1.0' if Gem.win_platform?
end

# Performance and Optimization
gem 'faraday-retry'

# Pinned Versions for Stability
gem 'liquid', '4.0.4'
gem 'safe_yaml', '1.0.5'
