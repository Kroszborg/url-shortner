/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  experimental: {
    appDir: true,
  },
  // Ignore ESLint errors during build
  eslint: {
    ignoreDuringBuilds: true,
  },
  // Ignore TypeScript build errors (if applicable)
  typescript: {
    ignoreBuildErrors: true,
  },
}

module.exports = nextConfig