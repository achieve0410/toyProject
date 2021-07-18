import React from 'react';  // jsx 문법을 쓰기 위해 필요
import ReactDOM from 'react-dom'; // 앱 랜더링을 위해 필요. 엔트리 포인트에서 쓰이고, 브라우저 뿐 아니라 서버사이드에서도 사용됨
import './index.css'; // css 파일을 Import해서 사용
import App2 from './App2';
import App from './App'; // app 이라는 react component를 가져올 때 사용
                         // component는 웹에서 기본적인 화면을 구성하는 단위
                         // 예를 들면 회원가입 화면에서 button, input, textarea 같은 것부터 이들로 구성된 화면 또한 component
import reportWebVitals from './reportWebVitals'; // 리소스 캐싱을 통해서 오프라인 혹은 느린 통신 간에도 화면을 보여주기 위해 사용

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root') // root id를 가진 태그를 찾아서 App component 안에 렌더링 시킴
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
