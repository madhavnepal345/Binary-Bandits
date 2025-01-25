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
    <div className="mx-4 flex gap-4 justify-between items-center h-[100vh]">
      {/* left Sidebar  */}
      <Leftbar/>

      {/* Right bar  */}
      <Rightbar />
    </div>
  );
}
