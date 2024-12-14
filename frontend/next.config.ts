/** @type {import('next').NextConfig} */
const nextConfig = {
  // Disable telemetry
  telemetry: {
    disabled: true
  },
  // Ignore build errors
  typescript: {
    ignoreBuildErrors: true
  },
  eslint: {
    ignoreDuringBuilds: true
  }
};

module.exports = nextConfig;