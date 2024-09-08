<script lang="ts">
	import { checkAccountAndRedirect } from "$lib/store";
	import { page } from "$app/stores";
	import { getResumesByMemberId} from '$lib/api/resume';
	import { onMount } from 'svelte';
	import AppPdf from '../pdf/AppPdf.svelte';
	import Page from '../pdf/Page.svelte';
	import { account } from '$lib/store';
	import type {Resume} from "$lib/interfaces/resume/Resume"
	import { writable } from "svelte/store";
	import type PersonalInfo from "$lib/interfaces/resume/PersonalInfo"
	import Skill from "$lib/components/resume/Skill.svelte";
	import ProfessionalExp from "$lib/components/resume/ProfessionalExp.svelte";
	import Link from "$lib/components/resume/Link.svelte";
	import Award from "$lib/components/resume/Award.svelte";
	import Certificate from "$lib/components/resume/Certificate.svelte";
	import Course from "$lib/components/resume/Course.svelte";
	import Education from "$lib/components/resume/Education.svelte";
	import Interest from "$lib/components/resume/Interest.svelte";
	import Language from "$lib/components/resume/Language.svelte";
	import Project from "$lib/components/resume/Project.svelte";
	import Publication from "$lib/components/resume/Publication.svelte";
	import Reference from "$lib/components/resume/Reference.svelte";
  
	export const id = writable<number | null>(null);

	$: resumeId = Number($page.params.id);
  
	const loadPage = () => {
	};
  
	checkAccountAndRedirect(loadPage);
  
	let print = false;
	let resume: Resume | null = null;
	let resumePersonalInfo: PersonalInfo | null = null;
	let resumeSkill: Skill[] = [];
	let resumeProfessionalExp: ProfessionalExp[] = [];
	let resumeLink: Link[] = [];
	let resumeAward: Award[] = [];
	let resumeCertificate: Certificate[] = [];
	let resumeCourse: Course[] = [];
	let resumeEducation: Education[] = [];
	let resumeInterest: Interest[] = [];
	let resumeLanguage: Language[] = [];
	let resumeProject: Project[] = [];
	let resumePublication: Publication[] = [];
	let resumeReference: Reference[] = [];

  
	onMount(async () => {
	if (!$account) return;

	const resumes = await getResumesByMemberId($account.id);
	resume = resumes.find(r => r.id === resumeId);
	resumePersonalInfo = resume?.personal_info;
	resumeSkill = resume?.skills
	resumeProfessionalExp = resume?.professional_exps;
	resumeLink = resume?.links;
	resumeAward = resume?.awards;
	resumeCertificate = resume?.certificates;
	resumeCourse = resume?.courses;
	resumeEducation = resume?.educations;
	resumeInterest = resume?.interests;
	resumeLanguage = resume?.languages;
	resumeProject = resume?.projects;
	resumePublication = resume?.publications;
	resumeReference = resume?.references;
	});

	$: filteredInfoPersonalInfo = {
    fullName: resumePersonalInfo?.full_name || "",
	jobTitle: resumePersonalInfo?.job_title || "",
	email: resumePersonalInfo?.email || "",
	phoneNumber: resumePersonalInfo?.phone_number || ""
  };
  
	$: htmlStringPersonalInfo = `
	  <h2>Personal Information</h2>
	  <ul>
		<li><strong>Full Name:</strong> ${filteredInfoPersonalInfo.fullName}</li>
		<li><strong>Job Title:</strong> ${filteredInfoPersonalInfo.jobTitle}</li>
		<li><strong>Email:</strong> ${filteredInfoPersonalInfo.email}</li>
		<li><strong>Phone Number:</strong>${filteredInfoPersonalInfo.phoneNumber}</li>
	  </ul>`;
  </script>
  
  <section>
	<button on:click={() => (print = true)}>
		Print
	  </button>
	  <br /><br />
	  <h1>Resume</h1>
	<AppPdf bind:print={print}>
	  <Page>
		<div style="margin-top: 30px;">{@html htmlStringPersonalInfo} 
			<br />
			{#if resumeSkill.length > 0}
			<h2>Skills</h2>
			<ul>
				{#each resumeSkill as skill}
				<strong>Name:</strong> {skill.name} <br />
				<strong>Description:</strong> {skill.description} <br />
				<strong>Skill Level:</strong> {skill.skillLevel} <br /><br />
			  {/each}
		  </ul>
		  {/if}
		  {#if resumeProfessionalExp.length > 0}
		  <h2>Professional Experience</h2>
		  <ul>
			{#each resumeProfessionalExp as exp}
			<strong>Job Title</strong> {exp.job_title} <br />
			<strong>Employer</strong> {exp.employer} <br />
			<strong>City</strong> {exp.city} <br />
			<strong>Country</strong> {exp.country} <br />
			<strong>Start Date</strong> {exp.start_date} <br />
			<strong>End Date</strong> {exp.end_date} <br />
			<strong>Description</strong> {exp.description} <br /><br />
			{/each}
		  </ul>
		  {/if}
		  {#if resumeLink.length > 0}
		 <h2>Links</h2>
		 <ul>
			{#each resumeLink as link} 
			<strong>Title</strong> {link.title} <br />
			<strong>URL</strong> {link.url} <br /><br />
			{/each}
		 </ul> 
		  {/if}
		  {#if resumeAward.length > 0}
		  <h2>Awards</h2>
		  <ul>
			{#each resumeAward as award}
			<strong>Title</strong> {award.title} <br />
			<strong>Issuer</strong> {award.issuer} <br />
			<strong>Date</strong> {award.date} <br />
			<strong>Description</strong> {award.description} <br /><br />
			{/each}
		  </ul>
		  {/if}
		  {#if resumeCertificate.length > 0}
		  <h2>Certificates</h2>
		  <ul>
		 	 {#each resumeCertificate as certificate}
		 	 <strong>Name</strong> {certificate.name} <br />
		 	 <strong>Description</strong> {certificate.description} <br /><br />
			  {/each}
		  </ul>
		  {/if}
		  {#if resumeCourse.length > 0}
		  <h2>Courses</h2>
		  <ul>
			{#each resumeCourse as course}
			<strong>Degree</strong> {course.degree} <br />
			<strong>Institution</strong> {course.institution} <br />
			<strong>City</strong> {course.city} <br />
			<strong>Country</strong> {course.country} <br />
			<strong>Start Date</strong> {course.start_date} <br />
			<strong>End Date</strong> {course.end_date} <br />
			<strong>Description</strong> {course.description} <br /><br />
			{/each}
		  </ul>
		  {/if}
		  {#if resumeEducation}
		  <h2>Education</h2>
		  <ul>
			{#each resumeEducation as edu}
			<strong>Degree</strong> {edu.degree} <br />
			<strong>Institution</strong> {edu.institution} <br />
			<strong>City</strong> {edu.city} <br />
			<strong>Country</strong> {edu.country} <br />
			<strong>Start Date</strong> {edu.start_date} <br />
			<strong>End Date</strong> {edu.end_date} <br />
			<strong>Description</strong> {edu.description} <br /><br />
			{/each}
		  </ul>
		  {/if}
		  {#if resumeInterest.length > 0}
		  <h2>Interests</h2>
		  <ul>
			{#each resumeInterest as interest}
			<strong>Name</strong> {interest.name} <br />
			<strong>Description</strong> {interest.description} <br /><br />
			{/each}
		  </ul>
		  {/if}
		  {#if resumeLanguage.length > 0}
		  <h2>Languages</h2>
		  <ul>
			{#each resumeLanguage as lang}
			<strong>Language:</strong> {lang.language} <br />
			<strong>Description:</strong> {lang.description} <br />
			<strong>Skill Level:</strong> {lang.skillLevel} <br /><br />
			{/each}
		  </ul>
		  {/if}
		  {#if resumeProject.length > 0}
		  <h2>Projects</h2>
		  <ul>
			{#each resumeProject as project}
			<strong>Title:</strong> {project.title} <br />
			<strong>Subtitle:</strong> project.subtitle} <br />
			<strong>Start Date</strong> {project.start_date} <br />
			<strong>End Date</strong> {project.end_date} <br />
			<strong>Description:</strong> {project.description} <br /><br />
			{/each}
		  </ul>
		  {/if}
		  {#if resumePublication.length > 0}
		  <h2>Publications</h2>
		  <ul>
			{#each resumePublication as publication}
			<strong>Title:</strong> {publication.title} <br />
			<strong>Publisher:</strong> {publication.publisher} <br />
			<strong>Date:</strong> {publication.date} <br />
			<strong>Description</strong> {publication.description} <br /><br />
			{/each}
		  </ul>
		  {/if}
		  {#if resumeReference.length > 0}
		  <h2>References</h2>
		  <ul>
			{#each resumeReference as ref}
			<strong>Name:</strong> {ref.name} <br />
			<strong>Job Title:</strong> {ref.job_title} <br />
			<strong>Organization:</strong> {ref.organization} <br />
			<strong>Email:</strong> {ref.email} <br />
			<strong>Phone:</strong> {ref.phone} <br /><br />
			{/each}
		  </ul>
		  {/if}
	  </Page>
	</AppPdf>
  </section>