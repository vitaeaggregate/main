import { writable } from "svelte/store";
import type Account from "./interfaces/member/Account";

export const account = writable<Account | null>();
export const currentResume = writable<{
	id: number | null;
}>({
	id: null
});
