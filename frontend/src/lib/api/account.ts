import { PUBLIC_SERVER } from "$env/static/public";
import type Account from "$lib/interfaces/member/Account";
import { error } from "@sveltejs/kit";

export async function createOrGetAccount(token: string) {
  const fetchConfig: RequestInit = {
    method: "POST",
    headers: {
      "Content-Type": "applications/json",
      Authorization: `Bearer ${token}`
    }
  };

  const response = await fetch(PUBLIC_SERVER + "/firebase/accounts/", fetchConfig);

  if (!response.ok) throw error(response.status, response.statusText);

  const account: Account = await response.json();

  return account;
}
