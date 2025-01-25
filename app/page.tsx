import Leftbar from "@/components/Leftbar";
import Rightbar from "@/components/Rightbar";

export default function Home() {
  const buttons = [
    { name: "Subject" },
    { name: "ORM" },
    { name: "Voice Ars" },
    { name: "FAQ" },
  ];
  return (
    <div
      id="home"
      className="bg-gradient-to-r from-gray-500 to-blue-100 px-4 flex gap-4 justify-between items-center h-[100vh]"
    >
      {/* left Sidebar  */}
      <Leftbar />

      {/* Right bar  */}
      <Rightbar />
    </div>
  );
}
