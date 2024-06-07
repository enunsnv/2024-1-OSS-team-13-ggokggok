import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react-swc';

export default defineConfig({
  plugins: [react()],
  build: {
    outDir: 'build', // 출력 디렉토리를 'build'로 설정
  },
  server: {
    proxy: {
      '/v1': {
        target: 'https://openapi.naver.com/',
        changeOrigin: true,
    
      }
    }
  }
});
