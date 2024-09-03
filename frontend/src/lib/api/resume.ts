import { PUBLIC_SERVER } from "$env/static/public";
import type Resume from "$lib/interfaces/resume/Resume";
import { fetchData } from "$lib/utils";
import { error } from "@sveltejs/kit";

export const getResumesByMemberId = async (memberId: number): Promise<Resume[] | null> => {
	const requestInit: RequestInit = {
		method: "GET"
	};

	const response = await fetchData(
		PUBLIC_SERVER + "/members/" + memberId + "/resumes",
		requestInit
	);

	if (!response.ok) {
		return error(response.status, response.statusText);
	}

    const resumes: Resume[] = await response.json()

	return resumes.length ? resumes : null;
};
