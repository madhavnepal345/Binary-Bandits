import React from "react";

const Rightbar = () => {
  const buttons = [
    { name: "Subject" },
    { name: "ORM" },
    { name: "Voice Ars" },
    { name: "FAQ" },
  ];
  return (
    <div className="bg-gradient-to-r from-purple-200 to-gray-400 bg-[#B0A8A8] shadow-lg flex flex-col items-center gap-4 w-full rounded-lg h-[93%] px-4 py-3">
      {/* head  */}
      <div className="flex justify-between w-full text-lg">
        <div className="flex items-center justify-center font-semibold text-xl gap-2">
          <img
            src="/brainy.png"
            className="w-7 h-7 rounded-full "
            alt="brainy"
          />
          <h1>Brainy Bot</h1>
        </div>
        {/* <img className="bg-cover w-6 h-5" src="/help.png" alt="help" /> */}
        <div className="flex gap-2 items-center justify-center">
          <button className="bg-gradient-to-r from-gray-300 to-purple-100 shadow-md bg-[#8D8C8C] text-base font-semibold border-black px-5 rounded-lg py-[6px]">
            Login
          </button>
          <button className="bg-gradient-to-r text-base from-gray-300 to-purple-100 shadow-md bg-[#8D8C8C] font-semibold border-black px-5 rounded-lg py-[6px]">
            SignUp
          </button>
        </div>
      </div>

      {/* Optional head  */}
      <div className="flex self-start mx-[50px] gap-4">
        {buttons.map((data, index) => (
          <button
            className="bg-gradient-to-r from-purple-100 to-gray-300 bg-[#8D8C8C] shadow-md px-[5px] py-[8px] w-[100px] rounded-lg border-black font-semibold"
            key={index}
          >
            {data.name}
          </button>
        ))}
      </div>

      {/* ChatBox  */}
      <div className="bg-gradient-to-r from-purple-100 to-gray-300 text-center flex items-center justify-center text-xl shadow-md w-[90%] h-full rounded-lg py-4 px-4 font-semibold">
        ...✋ Hello World ✋...
      </div>

      {/* Prompt Box  */}
      <div className="bg-gradient-to-r from-purple-200 to-gray-200 shadow-md flex items-center justify-between w-[90%] bg-[#8D8C8C] rounded-lg py-4 px-3 overflow-hidden">
        <div className="flex items-center gap-3 justify-center">
          <img className="cursor-pointer" src="/mic.png" alt="microphone" />
          <input
            className="bg-transparent text-black placeholder:font-semibold placeholder-black outline-none border-none w-[100vh]"
            type="text"
            placeholder="Enter your prompts here..."
          />
        </div>
        <div className="flex items-center justify-center gap-3">
          <img className="cursor-pointer" src="/send.png" alt="send" />
          <img className="cursor-pointer" src="/gif.png" alt="gif" />
          <img className="cursor-pointer" src="/image.png" alt="image" />
        </div>
      </div>
    </div>
  );
};

export default Rightbar;
