import type { Config } from "tailwindcss";

export default {
  content: ["./src/**/*.{html,js,svelte,ts}"],

  theme: {
    extend: {
      colors: {
        green: "#588157",
        lime: "#A3B18A"
      }
    }
  },

  plugins: [require("@tailwindcss/typography")]
} as Config;
