import puppeteer from "puppeteer-core";
import chromium from "@sparticuz/chromium";
import type { RequestHandler } from "@sveltejs/kit";

export const POST: RequestHandler = async ({ request }) => {
  const { body } = await request.json();
  const browser = await puppeteer.launch({
    args: chromium.args,
    executablePath: await chromium.executablePath(),
    headless: true
  });
  
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
