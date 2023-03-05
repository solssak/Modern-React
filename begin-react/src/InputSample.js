import React, { useState } from "react";

function InputSample() {
  const [inputs, setinputs] = useState({
    name: "",
    nickname: "",
  });

  const { name, nickname } = inputs;

  const onChange = (e) => {
    const { name, value } = e.target;
    setinputs({
      ...inputs,
      [name]: value, // 이 부분을 잘 모르겠다.  >> 객체 동적 접근
    });
  };

  const onReset = () => {
    setinputs({
      name: "",
      nickname: "",
    });
  };

  return (
    <div>
      <input name="name" placeholder="이름" onChange={onChange} value={name} />
      <input
        name="nickname"
        placeholder="닉네임"
        onChange={onChange}
        value={nickname}
      />
      <button onClick={onReset}>초기화</button>
      <div>
        <b>값: </b>
        {name} ({nickname})
      </div>
    </div>
  );
}

export default InputSample;
