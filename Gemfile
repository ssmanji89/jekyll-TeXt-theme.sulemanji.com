source 'https://rubygems.org'

# Core Jekyll and GitHub Pages
gem 'github-pages', group: :jekyll_plugins
gem 'jekyll', '~> 3.9.5'

# Theme (with remote and local options)
gem 'jekyll-text-theme'
gem 'jekyll-remote-theme'

# Plugins
group :jekyll_plugins do
  gem 'jekyll-feed'
  gem 'jekyll-paginate'
  gem 'jekyll-sitemap'
  gem 'jekyll-seo-tag'
  gem 'jekyll-redirect-from'
  gem 'jemoji'
  gem 'jekyll-include-cache'
end

# Compatibility and Performance
gem 'webrick'
gem 'faraday-retry'

# Development and Platform Support
group :development do
  gem 'wdm', '>= 0.1.0' if Gem.win_platform?
end

# Pinned versions for stability
gem 'kramdown', '~> 2.3.1'
gem 'kramdown-parser-gfm', '~> 1.1.0'
