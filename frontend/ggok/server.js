const express = require('express');
const { createProxyMiddleware } = require('http-proxy-middleware');
const path = require('path');

const app = express();

// 프록시 설정
app.use('/api', createProxyMiddleware({
  target: 'https://openapi.naver.com',
  changeOrigin: true,
  pathRewrite: {
    '^/vi': '',
  },
}));

// 정적 파일 제공 (빌드된 파일)
app.use(express.static(path.join(__dirname, 'build')));

app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, 'build', 'index.html'));
});

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
