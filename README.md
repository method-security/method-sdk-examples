# Method SDK Examples

This repository contains example implementations of the Method SDK across multiple programming languages.

## Structure

```
method-sdk-examples/
├── python/          # Python examples using methodsdk
└── README.md       # This file
```

## Getting Started

Each language directory contains its own implementation and setup instructions:

### Python

- **Location**: `./python/`
- **Dependencies**: Uses UV for package management
- **Setup**: See `python/README.md` for detailed instructions
- **Features**: Environment variable configuration, basic API client setup

### Other Languages

Coming soon! Each will include:

- Language-specific package/dependency management
- Environment configuration
- Basic API client examples
- Language-specific best practices

## Environment Configuration

Each language implementation uses environment variables for configuration:

- `OAUTH_CLIENT_ID`: Your Method Security client ID
- `OAUTH_CLIENT_SECRET`: Your Method Security client secret
- `METHOD_URL`: API endpoint URL

## Contributing

When adding examples for a new language:

1. Create a new directory for the language
2. Include a language-specific README with setup instructions
3. Follow the same environment variable pattern
4. Include basic examples of SDK usage
5. Update this main README
