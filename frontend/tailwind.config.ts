import type { Config } from "tailwindcss";

export default {
  content: ["./src/**/*.{html,js,svelte,ts}"],

  theme: {
    extend: {
      colors: {
        lime: "#cbc62c",
        orange: "#F2F1F1",
        green: "#A4BD17",
        grayish: "#B2B2B2",
        red: "#BD2B17"
      },
      maxHeight: {
        "128": "32rem"
      }
    }
  },

  plugins: [require("@tailwindcss/typography")]
} as Config;
