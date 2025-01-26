import Link from "next/link";
import React from "react";

const Leftbar = () => {
  const sidebarData = [
    {
      name: "About",
      src: "/about.png",
      href: "/about",
    },
    {
      name: "Help",
      src: "/help.png",
      href: "/help",
    },
    {
      name: "Activity",
      src: "/activity.png",
      href: "/activity",
    },
    {
      name: "Settings",
      src: "/setting.png",
      href: "/setting",
    },
    {
      name: "Contact Us",
      src: "/contactus.png",
      href: "/map",
    },
  ];
  return (
    <div className="bg-gradient-to-r from-gray-400 to-purple-200 flex flex-col justify-between shadow-lg bg-[#B0A8A8] h-[93%] w-[400px] rounded-lg px-5 py-2">
      <div className="flex gap-5 items-center justify-between">
        <img className="cursor-pointer" src="/sidebar.png" alt="sidebar" />
        <h1 className="cursor-pointer text-center font-semibold text-xl drop-shadow-md">
          Accessories
        </h1>
        <img className="pl-6 cursor-pointer" src="/search.png" alt="search" />
        <img
          className="w-6 h-6 cursor-pointer"
          src="/fourdots.png"
          alt="fourdots"
        />
      </div>
      <div className="flex flex-col gap-2 h-[45%] rounded-lg">
        <div className="w-[120px] flex items-center justify-center gap-2 bg-gradient-to-r from-gray-300 to-purple-100 shadow-md bg-[#8D8C8C] px-2 border-black rounded-lg py-2 mt-2">
          <img src="/plus.png" alt="plus" className="w-[13px] h-[13px]" />
          <h2 className="font-semibold">New Chat</h2>
        </div>
        <h2 className="font-semibold text-lg py-2">Recent Activity :</h2>
        <ol
          type="1"
          className="font-semibold text-[16.5px] flex flex-col gap-3"
        >
          <li>1). Tell Me About Sutainable Development.</li>
          <li>2). What is waste management?</li>
          <li>3). How can we contribute in supply chain management.</li>
        </ol>
      </div>
      <div className="w-full h-[1px] opacity-55 border-[0.2px] border-black"></div>
      <div>
        {/* Links and Info */}
        <div className="flex flex-col gap-3 relative top-[8px]">
          {sidebarData.map((data, index) => (
            <div className="flex items-center gap-5" key={index}>
              <img
                className="cursor-pointer w-5 h-5 flex"
                src={data.src}
                alt={data.name}
              />
              <Link href={data.href} className="text-md font-semibold">
                {data.name}
              </Link>
            </div>
          ))}
        </div>
      </div>

      {/* Map  */}
      <div className="pt-10 font-semibold">
        <Link href="/map" className="text-xs">
          <p>Dharan, Nepal</p>
          From your IP address . Update location
        </Link>
      </div>
    </div>
  );
};

export default Leftbar;
