import type Resume from "$lib/interfaces/resume/Resume";
import { memberID } from "../../routes/resumes/+page.svelte"
// "../../routes/my/resumes/+page.svelte"

const endPoint = import.meta.env.BASE_URL + "/members/" + memberID + "/resumes";

// POST Resume Data
export const addResume = async (resume: Resume) => {
	const response = await fetch(endPoint, {
		method: "POST",
		body: JSON.stringify(resume)
	});
	const json = await response.json();
	return JSON.stringify(json);
};

// DELETE Resume Data
