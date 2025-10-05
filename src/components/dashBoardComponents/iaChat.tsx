import React from "react";

const iaChat = () => {
  return (
    <div className="flex flex-col justify-center">
      <div className="flex flex-row w-[100%] h-[65vh]">
        <div className="w-[100%] h-full overflow-auto pl-[5%] pr-2 mr-2 mt-4">
          <p className="text-white font-600">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit.
            Pellentesque eleifend... Sed ut perspiciatis unde omnis iste natus
            error sit voluptatem accusantium doloremque laudantium... Sed ut
            perspiciatis unde omnis iste natus error sit voluptatem accusantium
            doloremque laudantium... Sed ut perspiciatis unde omnis iste natus
            error sit voluptatem accusantium doloremque laudantium... Sed ut
            perspiciatis unde omnis iste natus error sit voluptatem accusantium
            doloremque laudantium... Sed ut perspiciatis unde omnis iste natus
            error sit voluptatem accusantium doloremque laudantium... Sed ut
            perspiciatis unde omnis iste natus error sit voluptatem accusantium
            doloremque laudantium... Sed ut perspiciatis unde omnis iste natus
            error sit voluptatem accusantium doloremque laudantium... Sed ut
            perspiciatis unde omnis iste natus error sit voluptatem accusantium
            doloremque laudantium... Lorem ipsum dolor sit amet, consectetur
            adipiscing elit. Pellentesque eleifend... Sed ut perspiciatis unde
            omnis iste natus error sit voluptatem accusantium doloremque
            laudantium... Sed ut perspiciatis unde omnis iste natus error sit
            voluptatem accusantium doloremque laudantium... Sed ut perspiciatis
            unde omnis iste natus error sit voluptatem accusantium doloremque
            laudantium... Sed ut perspiciatis unde omnis iste natus error sit
            voluptatem accusantium doloremque laudantium... Sed ut perspiciatis
            unde omnis iste natus error sit voluptatem accusantium doloremque
            laudantium... Sed ut perspiciatis unde omnis iste natus error sit
            voluptatem accusantium doloremque laudantium... Sed ut perspiciatis
            unde omnis iste natus error sit voluptatem accusantium doloremque
            laudantium... Sed ut perspiciatis unde omnis iste natus error sit
            voluptatem accusantium doloremque laudantium... Lorem ipsum dolor
            sit amet, consectetur adipiscing elit. Pellentesque eleifend... Sed
            ut perspiciatis unde omnis iste natus error sit voluptatem
            accusantium doloremque laudantium... Sed ut perspiciatis unde omnis
            iste natus error sit voluptatem accusantium doloremque laudantium...
            Sed ut perspiciatis unde omnis iste natus error sit voluptatem
            accusantium doloremque laudantium... Sed ut perspiciatis unde omnis
            iste natus error sit voluptatem accusantium doloremque laudantium...
            Sed ut perspiciatis unde omnis iste natus error sit voluptatem
            accusantium doloremque laudantium... Sed ut perspiciatis unde omnis
            iste natus error sit voluptatem accusantium doloremque laudantium...
            Sed ut perspiciatis unde omnis iste natus error sit voluptatem
            accusantium doloremque laudantium... Sed ut perspiciatis unde omnis
            iste natus error sit voluptatem accusantium doloremque laudantium...
          </p>
        </div>
      </div>
      <div className="flex flex-col justify-content w-[100%] h-[15vh] pt-[4vh]">
        <div className="bg-white w-[90%] h-[.1px] rounded-full ml-[5%]"></div>
        <div className="flex flex-row">
          <div className="flex items-center w-[100%] h-[10vh]">
            <textarea
              id="name"
              placeholder=" "
              className="flex items-center ml-[5%] w-[100%] h-[80%] peer border-none rounded-md outline-none resize-none"
            />
            <label
              htmlFor="name"
              className="absolute left-10 text-white peer-placeholder-shown:opacity-100 peer-focus:opacity-0 peer-placeholder-shown:opacity-100 peer-placeholder-shown:translate-y-0 opacity-0"
            >
              {"Pesquisar"}
            </label>
          </div>
          <div className="flex items-center text-center mr-[5%]">
            <button className="h-[5vh] w-[3vw] bg-white text-blue-200 rounded-xl text-center cursor-pointer text-lg items-center">
              {">"}
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default iaChat;
