import { test, expect } from "@playwright/test";

test("can login", async ({ page }) => {
  await page.goto("http://localhost:5173");

  await page.getByPlaceholder("Email").fill("brandoncook2289@yahoo.com");
  await page.getByPlaceholder("Password").fill("admin123");

  await page.getByRole("button").nth(0).click();
  await page.waitForURL("http://localhost:5173/community");

  expect(page.url() === "http://localhost:5173/community");
});

test("can logout", async ({ page }) => {
  await page.goto("http://localhost:5173");

  await page.getByPlaceholder("Email").fill("brandoncook2289@yahoo.com");
  await page.getByPlaceholder("Password").fill("admin123");

  await page.getByRole("button").nth(0).click();
  await page.waitForURL("http://localhost:5173/community");
  await page.locator('button:text("Logout")').click();
  await page.waitForURL("http://localhost:5173/login");

  expect(page.url() === "http://localhost:5173/login");
});
