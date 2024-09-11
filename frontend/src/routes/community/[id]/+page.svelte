<script lang="ts">
	import type { Comment } from "$lib/interfaces/resume/Comment";
	import { writable } from "svelte/store";
	import { deleteComment, getCommentsByMemberIdByResumeId } from "$lib/api/comment";
	import { getResumesByResumeId } from "$lib/api/resume";
	import { account, checkAccountAndRedirect } from "$lib/store";
	import { page } from "$app/stores";
	import NewComment from "$lib/components/resume/comment.svelte";
	// import { onMount } from "svelte";
	// import { getResumesByMemberId } from "$lib/api/resume";

	import type { Resume } from "$lib/interfaces/resume/Resume";
	import MainButton from "$lib/components/MainButton.svelte";
	import { goto } from "$app/navigation";
	// import Skill from "$lib/components/resume/Skill.svelte";
	// import ProfessionalExp from "$lib/components/resume/ProfessionalExp.svelte";
	// import Link from "$lib/components/resume/Link.svelte";
	// import Award from "$lib/components/resume/Award.svelte";
	// import Certificate from "$lib/components/resume/Certificate.svelte";
	// import Course from "$lib/components/resume/Course.svelte";
	// import Education from "$lib/components/resume/Education.svelte";
	// import Interest from "$lib/components/resume/Interest.svelte";
	// import Language from "$lib/components/resume/Language.svelte";
	// import Project from "$lib/components/resume/Project.svelte";
	// import Publication from "$lib/components/resume/Publication.svelte";
	// import Reference from "$lib/components/resume/Reference.svelte";

	export const id = writable<number | null>(null);

	$: resumeId = Number($page.params.id);

	let resumes: Resume[] | null = null;
	let resumesComments: { [resumeId: number]: Comment[] } = {};

	const loadPage = async () => {
		if (!$account) return;
		resumes = await getResumesByResumeId(resumeId);

		for (let resume of resumes) {
			const comments = await getCommentsByMemberIdByResumeId($account.id, resume.id);
			resumesComments[resume.id] = comments;
		}
	};

	function handleDeleteComment(id: number, resumeId: number, commentId: number) {
		deleteComment(id, resumeId, commentId);
	}

	const handleGoBack = () => {
		goto("/community");
	};

	checkAccountAndRedirect(loadPage);
</script>

<main>
	<h1>Community</h1>
	<br />
	<MainButton on:click={handleGoBack}>Back</MainButton><br /><br />
	<div class="test-div flex justify-center">
		<div
			class="mb-16 ml-16 mr-16 flex h-screen w-4/5 flex-col overflow-y-auto border-2 border-solid border-black p-4"
		>
			{#if resumes}
				{#each resumes as resume}
					{#if resume.id == resumeId}
						{#if resume.skills === undefined}
							<br />
						{:else if resume.skills.length > 0}
							<h2 class="print:text-xl">Skills</h2>
							<ul class="text-base leading-8 print:text-sm print:leading-6">
								<ul>
									{#each resume.skills as skill}
										{#if skill.name}
											<strong>Name:</strong> {skill.name} <br />
										{:else}<br />{/if}
										<strong>Description:</strong>
										{skill.description} <br />
										<strong>Skill Level:</strong>
										{skill.skill_level} <br /><br />
									{/each}
								</ul>
							</ul>
						{/if}
						{#if resume.professional_exps === undefined}
							<br />
						{:else if resume.professional_exps.length > 0}
							<h2 class="print:text-xl">Professional Experience</h2>
							<ul class="text-base leading-8 print:text-sm print:leading-6">
								<ul>
									{#each resume.professional_exps as exp}
										{#if exp.job_title}
											<strong class="text-xl print:text-lg">{exp.job_title}</strong><br />
										{:else}<br />{/if}
										{#if exp.employer}
											<strong>Employer:</strong> {exp.employer} <br />
										{:else}<br />{/if}
										<strong>City:</strong>
										{exp.city} <br />
										<strong>Country:</strong>
										{exp.country} <br />
										<strong>Start Date:</strong>
										{exp.start_date} <br />
										<strong>End Date:</strong>
										{exp.end_date} <br />
										{#if exp.description}
											<strong>Description:</strong> {exp.description} <br /><br />
										{:else}<br />
										{/if}
									{/each}
								</ul>
							</ul>
						{/if}
						{#if resume.awards.length > 0}
							<h2 class="print:text-xl">Awards</h2>
							<ul class="text-base leading-8 print:text-sm print:leading-6">
								<ul>
									{#each resume.awards as award}
										{#if award.title}
											<strong>Title:</strong> {award.title} <br />
										{:else}<br />
										{/if}
										{#if award.issuer}
											<strong>Issuer:</strong> {award.issuer} <br />
										{:else}<br />
										{/if}
										{#if award.date}
											<strong>Date:</strong> {award.date} <br />
										{:else}<br />
										{/if}
										{#if award.description}
											<strong>Description:</strong> {award.description} <br /><br />
										{:else}<br />
										{/if}
									{/each}
								</ul>
							</ul>
						{/if}
						{#if resume.links === undefined}
							<br />
						{:else if resume.links.length > 0}
							<h2 class="print:text-xl">Links</h2>
							<ul class="text-base leading-8 print:text-sm print:leading-6">
								<ul>
									{#each resume.links as link}
										<strong>Title:</strong>
										{link.title} <br />
										<strong>URL:</strong>
										{link.url} <br /><br />
									{/each}
								</ul>
							</ul>
						{/if}
						{#if resume.certificates.length > 0}
							<h2 class="print:text-xl">Certificates</h2>
							<ul class="text-base leading-8 print:text-sm print:leading-6">
								<ul>
									{#each resume.certificates as certificate}
										{#if certificate.name}
											<strong>Name:</strong> {certificate.name} <br />
										{:else}<br />
										{/if}
										{#if certificate.description}
											<strong>Description:</strong> {certificate.description} <br /><br />
										{:else}<br />
										{/if}
									{/each}
								</ul>
							</ul>
						{/if}
						{#if resume.courses === undefined}
							<br />
						{:else if resume.courses.length > 0}
							<h2 class="print:text-xl">Courses</h2>
							<ul class="text-base leading-8 print:text-sm print:leading-6">
								<ul>
									{#each resume.courses as course}
										{#if course.degree}
											<strong>Degree:</strong> {course.degree} <br />
										{:else}<br />{/if}
										{#if course.institution}
											<strong>Institution:</strong> {course.institution} <br />
										{:else}<br />
										{/if}
										{#if course.city}
											<strong>City:</strong> {course.city} <br />
										{:else}<br />
										{/if}
										{#if course.country}
											<strong>Country:</strong> {course.country} <br />
										{:else}<br />
										{/if}
										{#if course.start_date}
											<strong>Start Date:</strong> {course.start_date} <br />
										{:else}<br />
										{/if}
										{#if course.end_date}
											<strong>End Date:</strong> {course.end_date} <br />
										{:else}<br />
										{/if}
										{#if course.description}
											<strong>Description:</strong> {course.description} <br /><br />
										{:else}<br />
										{/if}
									{/each}
								</ul>
							</ul>
						{/if}
						{#if resume.educations === undefined}
							<br />
						{:else if resume.educations.length < 0}
							<h2 class="print:text-xl">Education</h2>
							<ul class="text-base leading-8 print:text-sm print:leading-6">
								<ul>
									{#each resume.educations as edu}
										{#if edu.degree}
											<strong class="text-xl print:text-lg">{edu.degree}</strong><br />
										{:else}<br />
										{/if}
										{#if edu.institution}
											<strong>Institution:</strong> {edu.institution} <br />
										{:else}<br />
										{/if}
										{#if edu.city}
											<strong>City:</strong> {edu.city} <br />
										{:else}<br />
										{/if}
										{#if edu.country}
											<strong>Country:</strong> {edu.country} <br />
										{:else}<br />
										{/if}
										{#if edu.start_date}
											<strong>Start Date:</strong> {edu.start_date} <br />
										{:else}<br />
										{/if}
										{#if edu.end_date}
											<strong>End Date:</strong> {edu.end_date} <br />
										{:else}<br />
										{/if}
										{#if edu.description}
											<strong>Description:</strong> {edu.description} <br /><br />
										{:else}<br />
										{/if}
									{/each}
								</ul>
							</ul>
						{/if}
						{#if resume.interests === undefined}
							<br />
						{:else if resume.interests.length > 0}
							<h2 class="print:text-xl">Interests</h2>
							<ul class="text-base leading-8 print:text-sm print:leading-6">
								<ul>
									{#each resume.interests as interest}
										<strong>Name:</strong>
										{interest.name} <br />
										{#if interest.description}
											<strong>Description:</strong> {interest.description} <br /><br />
										{:else}<br />
										{/if}
									{/each}
								</ul>
							</ul>
						{/if}
						{#if resume.languages === undefined}
							<br />
						{:else if resume.languages.length > 0}
							<h2 class="print:text-xl">Languages</h2>
							<ul class="text-base leading-8 print:text-sm print:leading-6">
								<ul>
									{#each resume.languages as lang}
										<strong>Language:</strong>
										{lang.language} <br />
										<strong>Description:</strong>
										{lang.description} <br />
										<strong>Skill Level:</strong>
										{lang.skill_level} <br /><br />
									{/each}
								</ul>
							</ul>
						{/if}
						{#if resume.projects === undefined}
							<br />
						{:else if resume.projects.length > 0}
							<h2 class="print:text-xl">Projects</h2>
							<ul class="text-base leading-8 print:text-sm print:leading-6">
								<ul>
									{#each resume.projects as project}
										<strong>Title:</strong>
										{project.title} <br />
										{#if project.sub_title}
											<strong>Subtitle:</strong> {project.sub_title} <br />
										{:else}<br />
										{/if}
										{#if project.start_date}
											<strong>Start Date:</strong> {project.start_date} <br />
										{:else}<br />
										{/if}
										{#if project.end_date}
											<strong>End Date:</strong> {project.end_date} <br />
										{:else}<br />
										{/if}
										{#if project.description}
											<strong>Description:</strong> {project.description} <br /><br />
										{:else}<br />
										{/if}
									{/each}
								</ul>
							</ul>
						{/if}
						{#if resume.publications === undefined}
							<br />
						{:else if resume.publications.length > 0}
							<h2 class="print:text-xl">Publications</h2>
							<ul class="text-base leading-8 print:text-sm print:leading-6">
								<ul>
									{#each resume.publications as publication}
										<strong>Title:</strong>
										{publication.title} <br />
										{#if publication.publisher}
											<strong>Publisher:</strong> {publication.publisher} <br />
										{:else}<br />
										{/if}
										{#if publication.date}
											<strong>Date:</strong> {publication.date} <br />
										{:else}<br />
										{/if}
										{#if publication.description}
											<strong>Description</strong> {publication.description} <br /><br />
										{:else}<br />
										{/if}
									{/each}
								</ul>
							</ul>
						{/if}
					{/if}
				{/each}
			{/if}
		</div>
	</div>
	<h2>Comments</h2>
	<div class="flex justify-center">
		<div class="h-3/5 w-4/5 overflow-y-auto p-6">
			<ul class="flex flex-col gap-5 p-5">
				{#each Object.entries(resumesComments) as [id, comments]}
					{#if +id === resumeId}
						<!-- <h2>Resume ID: {id}</h2> -->
						<ul>
							{#each comments as comment, index}
								<li class="bg-gray-200 p-4">{comment.description}</li>
								<br />
								<button
									class="float-right"
									on:click={() => {
										handleDeleteComment($account.id, resumeId, comment.id);
									}}>Delete</button
								>
								<br /><br />
							{/each}
						</ul>{/if}
				{/each}
			</ul>
		</div>
	</div>
	<h3 class="mb-2">New Comment</h3>
	<NewComment></NewComment>
</main>
