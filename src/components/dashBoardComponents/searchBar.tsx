import React from "react";

const SearchBar = () => {
  const href = "/dashboardNext";
  return (
    <div className="flex justify-center w-[100vw]">
      <div className="flex flex-col w-[40%] border-1 border-stone-200/60 rounded-xl bg-transparent ">
        <div className="h-[10vh] relative">
          <textarea
            id="name"
            placeholder=" "
            className="peer border-none rounded-md w-[95%] h-[9vh] ml-[1vw] mt-[1vh] outline-none pb-12 resize-none"
          />
          <label
            htmlFor="name"
            className="absolute left-3 top-1.5 text-stone-300 peer-placeholder-shown:opacity-100 peer-focus:opacity-0 peer-placeholder-shown:opacity-100 peer-placeholder-shown:translate-y-0 opacity-0 translate-y-[-0.5rem]"
          >
            {"Pesquisar"}
          </label>
        </div>
        <div className="flex text-center h-[6vh] justify-between my[1vh] ">
          <button className="cursor-pointer my-[1vh]">
            <div className="flex flex-row items-center ">
              <div className="border-1 border-white rounded-full w-[2vw] h-fit text-center mx-[.5vw] items-center">
                +
              </div>
              <div className="text-sm text-start align-center text-white ">
                Adicionar arquivo ou imagem
              </div>
            </div>
          </button>
          <div className="flex items-center text-center">
            <a href={href}>
              <button className="h-[5vh] w-[3vw] bg-white text-blue-200 rounded-xl text-center cursor-pointer text-lg items-center mx-[1vw]">
                {">"}
              </button>
            </a>
          </div>
        </div>
      </div>
    </div>
  );
};

export default SearchBar;
