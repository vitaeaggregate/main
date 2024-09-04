import { writable } from "svelte/store";
import type Account from "$lib/interfaces/member/Account";
import type { Resume } from "$lib/interfaces/resume/Resume";
import type { Comment } from "$lib/interfaces/resume/Comment";

export const account = writable<Account | null>(null);

export const isAuthenticated = writable<boolean>(true);

// This was currentResume
export const loadedResumes = writable<{
	[resumeId: number]: {
		resume: Resume;
		comments: { [commentId: number]: Comment };
	};
}>({});