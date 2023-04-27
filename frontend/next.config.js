/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  axios: {
    baseUrl: 'http://localhost:8000/api',
  }
}

module.exports = nextConfig
