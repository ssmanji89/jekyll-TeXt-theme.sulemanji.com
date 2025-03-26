source 'https://rubygems.org'

# Core Jekyll
gem 'jekyll', '~> 4.4.1'

# Theme
gem 'jekyll-text-theme'

# Plugins
group :jekyll_plugins do
  gem 'jekyll-feed'
  gem 'jekyll-paginate'
  gem 'jekyll-sitemap'
  gem 'jekyll-seo-tag'
  gem 'jekyll-redirect-from'
  gem 'jemoji'
end

# Windows and other dependencies
platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem 'tzinfo', '>= 1', '< 3'
  gem 'tzinfo-data'
end

# Performance-related
gem 'webrick', '~> 1.8'

# Development dependencies
group :development do
  gem 'wdm', '~> 0.1.1', platforms: [:mingw, :x64_mingw, :mswin]
end
