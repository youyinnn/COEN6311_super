import man1 from "@/assets/img/avatars/man-1.png";
import man2 from "@/assets/img/avatars/man-2.png";
import man3 from "@/assets/img/avatars/man-3.png";
import man4 from "@/assets/img/avatars/man-4.png";
import man5 from "@/assets/img/avatars/man-5.png";
import man6 from "@/assets/img/avatars/man-6.png";

import woman1 from "@/assets/img/avatars/woman-1.png";
import woman2 from "@/assets/img/avatars/woman-2.png";
import woman3 from "@/assets/img/avatars/woman-3.png";
import woman4 from "@/assets/img/avatars/woman-4.png";
import woman5 from "@/assets/img/avatars/woman-5.png";
import woman6 from "@/assets/img/avatars/woman-6.png";

const avatars = [
  man1,
  man2,
  man3,
  man4,
  man5,
  man6,
  woman1,
  woman2,
  woman3,
  woman4,
  woman5,
  woman6,
];

const random = require("lodash.random");
const url =
  process.env.NODE_ENV === "development"
    ? "http://127.0.0.1:8000/scholar-hub/"
    : "http://concordia.youyinnn.top:8089/scholar-hub/";

const config = {
  paperSearchUrl: "https://api.semanticscholar.org/graph/v1/paper/search",
  paperDetailUrl: "https://api.semanticscholar.org/graph/v1/paper",

  testEnvBackEndUrl: url,
  avatars,
  getRandomAvatars: () => {
    return avatars[random(0, 11)];
  },
};

export default config;
