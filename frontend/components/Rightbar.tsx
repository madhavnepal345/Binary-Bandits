import React from "react";

const Rightbar = () => {
  const buttons = [
    { name: "Subject" },
    { name: "ORM" },
    { name: "Voice Ars" },
    { name: "FAQ" },
  ];
  return (
    <div className="bg-[#B0A8A8] flex flex-col items-center gap-4 w-full rounded-lg h-[93%] px-4 py-3">
      {/* head  */}
      <div className="flex items-center justify-between w-full text-lg">
        <h1 className="font-semibold justify-start">Brainy Bot</h1>
        {/* <img className="bg-cover w-6 h-5" src="/help.png" alt="help" /> */}
        <div className="flex gap-2 items-center justify-center">
          <button className="border-[1px] border-black px-3 rounded-lg py-1">
            Login
          </button>
          <button className="border-[1px] border-black px-3 rounded-lg py-1">
            SignUp
          </button>
        </div>
      </div>

      {/* Optional head  */}
      <div className="flex justify-center gap-4">
        {buttons.map((data, index) => (
          <button
            className="bg-[#8D8C8C] px-2 py-2 w-[120px] border-[1px] rounded-lg border-black font-semibold tracking-widest"
            key={index}
          >
            {data.name}
          </button>
        ))}
      </div>

      {/* ChatBox  */}
      <div className="text-center text-lg bg-[#8D8C8C] w-[90%] h-full rounded-lg py-4 px-4 font-semibold">
        Hello World ...
      </div>

      {/* Prompt Box  */}
      <div className="flex items-center justify-between w-[90%] bg-[#8D8C8C] rounded-lg py-3 px-3">
        <div className="flex items-center gap-3 justify-center">
          <img className="cursor-pointer" src="/mic.png" alt="microphone" />
          <input
            className="bg-[#8D8C8C] text-black placeholder-black outline-none border-none w-[100vh]"
            type="text"
            placeholder="Enter your prompts here..."
          />
        </div>
        <div className="flex items-center justify-center gap-3">
          <img className="cursor-pointer" src="/gif.png" alt="gif" />
          <img className="cursor-pointer" src="/image.png" alt="image" />
        </div>
      </div>
    </div>
  );
};

export default Rightbar;
