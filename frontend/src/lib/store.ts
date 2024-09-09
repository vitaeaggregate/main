import { writable } from "svelte/store";
import type Account from "$lib/interfaces/member/Account";
import type { Resume } from "$lib/interfaces/resume/Resume";
import type { Comment } from "$lib/interfaces/resume/Comment";
import { goto } from "$app/navigation";

export const account = writable<Account | null>();

// This was currentResume
export const loadedResumes = writable<{
	[resumeId: number]: {
		resume: Resume;
		comments: { [commentId: number]: Comment };
	};
}>({});

export const checkAccountAndRedirect = (loadPage?: () => void) => {
	account.subscribe(($account) => {
		if ($account && Object.keys($account).length && loadPage) loadPage();
		else if ($account === null || ($account && !Object.keys($account).length))
			goto("/login", { replaceState: false });
	});
};
