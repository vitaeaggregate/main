import type { Config } from "tailwindcss";

export default {
  content: ["./src/**/*.{html,js,svelte,ts}"],

  theme: {
    extend: {
      colors: {
        lime: "#A3B18A",
        orange: "#F2F1F1"
      }
    }
  },

  plugins: [require("@tailwindcss/typography")]
} as Config;
