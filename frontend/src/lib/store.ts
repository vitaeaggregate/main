import { writable } from "svelte/store";
import type Account from "$lib/interfaces/member/Account";
import type { Resume } from "$lib/interfaces/resume/Resume";

export const account = writable<Account | null>();

export const loadedResumes = writable<Resume[] | null>();
