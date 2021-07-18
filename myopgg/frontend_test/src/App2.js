import React, { Component } from 'react';

function App2(props) {
    if (props.name=='123') {
        return <div>Hi {props.name}</div>
    } else {
        return <div>안녕하세요 {props.name}</div>
    }
}

App2.defaultProps = {
    name: '이름없음'
}

export default App2;