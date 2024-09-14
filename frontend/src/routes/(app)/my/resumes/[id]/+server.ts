import puppeteer from "puppeteer-core";
import chromium from "@sparticuz/chromium";
import type { RequestHandler } from "@sveltejs/kit";

export const POST: RequestHandler = async ({ request }) => {
  let { body } = await request.json();
  const browser = await puppeteer.launch({
    args: chromium.args,
    executablePath: await chromium.executablePath(),
    headless: true
  });

  const normalizeCssLink =
    "<link rel='https://necolas.github.io/normalize.css/8.0.1/normalize.css' />";

  const tailwindLink = "<script src='https://cdn.tailwindcss.com'></script>";

  body = normalizeCssLink + tailwindLink + body;

  const page = await browser.newPage();

  await page.setContent(body, { waitUntil: "networkidle0" });

  const pdfBuffer = await page.pdf({
    format: "A4"
  });

  await browser.close();

  return new Response(pdfBuffer, {
    headers: {
      "Content-Type": "applications/pdf",
      "Content-Disposition": "attachment; filename='resume.pdf'"
    }
  });
};
