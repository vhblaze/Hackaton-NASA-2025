import Image from "next/image";
import IaChat from "@/components/dashBoardComponents/iaChat";

export default function dashboardNext() {
  const dashboardOne = "/dashBoard";

  return (
    <div>
      <div className="flex flex-col w-[100vw] h-[100vh] overflow-hidden">
        <div className="flex justify-end w-[100vw]">
          <div>
            <a href={dashboardOne}>
              <p className="my-[1vh] mx-[1vw] font-light italic font-inter text-[40px] w-fit [text-shadow:_-2px_2px_8px_rgba(255,255,255,0.4)]">
                SACY TECH.
              </p>
            </a>
          </div>
        </div>
        <div className="flex flex-row w-full gap-5 ml-[1vw] overflow-hidden">
          <div className="bg-transparent h-[80vh] w-[35vw] border-1 border-white opacity-90 rounded-xl"><IaChat /></div>
          <div className="bg-red-500 h-[80vh] w-[50vw]">aa</div>
          <div className="bg-red-500 h-[80vh] w-[10vw]">aa</div>
        </div>
      </div>
    </div>
  );
}
