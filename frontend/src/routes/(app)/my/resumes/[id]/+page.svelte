<script lang="ts">
  import { page } from "$app/stores";
  import { deleteResume, getResumesByMemberId } from "$lib/api/resume";
  import AppPdf from "../pdf/AppPdf.svelte";
  import Page from "../pdf/Page.svelte";
  import { account } from "$lib/store";
  import type { Resume } from "$lib/interfaces/resume/Resume";
  import type PersonalInfo from "$lib/interfaces/resume/PersonalInfo";
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
  import { goto } from "$app/navigation";
  import MainButton from "$lib/components/MainButton.svelte";

  let print = false;
  let resume: Resume | undefined = undefined;
  let resumePersonalInfo: PersonalInfo | undefined = undefined;
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

  const loadPage = async () => {
    if (!$account) return;

    const resumes = await getResumesByMemberId($account.id);
    resume = resumes.find((r) => r.id === resumeId);

    if (resume) {
      resumePersonalInfo = resume?.personal_info;
      resumeSkill = resume?.skills as Skill[];
      resumeProfessionalExp = resume?.professional_exps as ProfessionalExp[];
      resumeLink = resume?.links as Link[];
      resumeAward = resume?.awards as Award[];
      resumeCertificate = resume?.certificates as Certificate[];
      resumeCourse = resume?.courses as Course[];
      resumeEducation = resume?.educations as Education[];
      resumeInterest = resume?.interests as Interest[];
      resumeLanguage = resume?.languages as Language[];
      resumeProject = resume?.projects as Project[];
      resumePublication = resume?.publications as Publication[];
      resumeReference = resume?.references as Reference[];
    }
  };

  function handleResumeDelete(id: number, resumeId: number) {
    deleteResume(resumeId);
    goto("/my/page");
  }

  function handleResumeEdit(resumeId: number) {
    goto(`/my/resumes/${resumeId}/edit`);
  }

  $: resumeId = Number($page.params.id);

  $: if ($account && $page.params.id) loadPage();
</script>

{#if $account && $page.params.id}
  <section>
    <h1>Resume</h1>

    <br />
    <MainButton
      on:click={() => {
        handleResumeEdit(resumeId);
      }}>Edit</MainButton
    >
    <MainButton on:click={() => handleResumeDelete($account.id, resumeId)}>Delete</MainButton>
    <MainButton on:click={() => (print = true)}>Print</MainButton>
    <br />
    <br />
    <AppPdf bind:print>
      <div
        class="mb-16 ml-16 mr-16 flex h-screen flex-col overflow-y-auto border-2 border-solid border-black p-4 print:m-0 print:-ml-12 print:-mr-12 print:overflow-y-visible print:border-none"
      >
        <Page>
          <ul class=" p-4 text-center font-sans">
            <div class="text-4xl font-medium">{resumePersonalInfo?.full_name}</div>
            <br />
            <div class="text-2xl">{resumePersonalInfo?.job_title}</div>
          </ul>
          <hr class="border-2 border-solid border-black" />
          <br />

          <h2 class="bg-gray-100 print:text-xl">Personal Info</h2>
          <ul class="text-base leading-8 print:text-sm print:leading-6">
            {#if resumePersonalInfo?.email}
              <li><strong>Email:</strong> {resumePersonalInfo?.email}</li>
            {/if}
            {#if resumePersonalInfo?.phone_number}
              <li><strong>Phone:</strong> {resumePersonalInfo?.phone_number}</li>
            {/if}
            {#if resumePersonalInfo?.address}
              <li><strong>Address:</strong> {resumePersonalInfo?.address}</li>
            {/if}
            {#if resumePersonalInfo?.date_of_birth}
              <li><strong>Date of Birth:</strong> {resumePersonalInfo?.date_of_birth}</li>
            {/if}
            {#if resumePersonalInfo?.driving_license}
              <li><strong>Driving License:</strong> {resumePersonalInfo?.driving_license}</li>
            {/if}
            {#if resumePersonalInfo?.gender_pronoun}
              <li><strong>Gender Pronouns:</strong> {resumePersonalInfo?.gender_pronoun}</li>
            {/if}
            {#if resumePersonalInfo?.marital_status}
              <li><strong>Marital Status:</strong> {resumePersonalInfo?.marital_status}</li>
            {/if}
            {#if resumePersonalInfo?.nationality}
              <li><strong>Nationality:</strong> {resumePersonalInfo?.nationality}</li>
            {/if}
          </ul>
          <br />
          {#if resumeSkill.length > 0}
            <h2 class="bg-gray-100 print:text-xl">Skills</h2>
            <ul class="text-base leading-8 print:text-sm print:leading-6">
              <ul>
                {#each resumeSkill as skill}
                  {#if skill.name}
                    <strong>Name:</strong> {skill.name} <br />
                  {/if}
                  {#if skill.description}
                    <strong>Description:</strong>
                    {skill.description} <br />
                  {/if}
                  {#if skill.skill_level}
                    <strong>Skill Level:</strong>
                    {skill.skill_level} <br />
                  {/if}
                  <br />
                {/each}
              </ul>
            </ul>
          {/if}
          {#if resumeProfessionalExp.length > 0}
            <h2 class="bg-gray-100 print:text-xl">Professional Experience</h2>
            <ul class="text-base leading-8 print:text-sm print:leading-6">
              <ul>
                {#each resumeProfessionalExp as exp}
                  <span class="float-right mr-2">
                    {#if exp.start_date}
                      {exp.start_date}
                    {/if}
                    -
                    {#if exp.end_date}
                      {exp.end_date} <br />
                    {/if}</span
                  >
                  {#if exp.job_title}
                    <strong class="text-xl print:text-lg">{exp.job_title}</strong><br />
                  {/if} -
                  {#if exp.city}<i>{exp.city}</i>{/if}{#if exp.city && exp.country},
                  {/if}
                  {#if exp.country}
                    <i>{exp.country}</i>
                  {/if}
                  <br />
                  {#if exp.employer}
                    <strong>Employer:</strong> {exp.employer} <br />
                  {/if}
                  {#if exp.description}
                    <strong>Description:</strong> {exp.description} <br /><br />
                  {/if}
                {/each}
              </ul>
            </ul>
          {/if}
          {#if resumeLink.length > 0}
            <h2 class="bg-gray-100 print:text-xl">Links</h2>
            <ul class="text-base leading-8 print:text-sm print:leading-6">
              <ul>
                {#each resumeLink as link}
                  <strong>Title:</strong>
                  {link.title} <br />
                  <strong>URL:</strong>
                  {link.url} <br /><br />
                {/each}
              </ul>
            </ul>
          {/if}
          {#if resumeAward.length > 0}
            <h2 class="bg-gray-100 print:text-xl">Awards</h2>
            <ul class="text-base leading-8 print:text-sm print:leading-6">
              <ul>
                {#each resumeAward as award}
                  {#if award.title}
                    <strong>Title:</strong> {award.title} <br />
                  {/if}
                  {#if award.issuer}
                    <strong>Issuer:</strong> {award.issuer} <br />
                  {/if}
                  {#if award.date}
                    <strong>Date:</strong> {award.date} <br />
                  {/if}
                  {#if award.description}
                    <strong>Description:</strong> {award.description} <br /><br />
                  {/if}
                {/each}
              </ul>
            </ul>
          {/if}
          {#if resumeCertificate.length > 0}
            <h2 class="bg-gray-100 print:text-xl">Certificates</h2>
            <ul class="text-base leading-8 print:text-sm print:leading-6">
              <ul>
                {#each resumeCertificate as certificate}
                  {#if certificate.name}
                    <strong>Name:</strong> {certificate.name} <br />
                  {/if}
                  {#if certificate.description}
                    <strong>Description:</strong> {certificate.description} <br /><br />
                  {/if}
                {/each}
              </ul>
            </ul>
          {/if}
          {#if resumeCourse.length > 0}
            <h2 class="bg-gray-100 print:text-xl">Courses</h2>
            <ul class="text-base leading-8 print:text-sm print:leading-6">
              <ul>
                {#each resumeCourse as course}
                  <span class="float-right mr-2">
                    {#if course.start_date}
                      {course.start_date}
                    {/if}
                    -
                    {#if course.end_date}
                      {course.end_date} <br />
                    {/if}</span
                  >
                  {#if course.degree}
                    <strong class="text-xl print:text-lg">{course.degree}</strong>
                  {/if} -
                  {#if course.city}<i>{course.city}</i>{/if}{#if course.city && course.country},
                  {/if}
                  {#if course.country}
                    <i>{course.country}</i>
                  {/if}
                  <br />
                  {#if course.institution}
                    <strong>Institution:</strong> {course.institution} <br />
                  {/if}
                  {#if course.description}
                    <strong>Description:</strong> {course.description} <br /><br />
                  {/if}
                {/each}
              </ul>
            </ul>
          {/if}
          {#if resumeEducation.length > 0}
            <h2 class="bg-gray-100 print:text-xl">Education</h2>
            <ul class="text-base leading-8 print:text-sm print:leading-6">
              <ul>
                {#each resumeEducation as edu}
                  <span class="float-right mr-2">
                    {#if edu.start_date}
                      {edu.start_date}
                    {/if}
                    -
                    {#if edu.end_date}
                      {edu.end_date} <br />
                    {/if}</span
                  >
                  {#if edu.degree}
                    <strong class="text-xl print:text-lg">{edu.degree}</strong>
                  {/if} -
                  {#if edu.city}<i>{edu.city}</i>{/if}{#if edu.city && edu.country},
                  {/if}
                  {#if edu.country}
                    <i>{edu.country}</i>
                  {/if}
                  <br />
                  {#if edu.institution}
                    <strong>Institution:</strong> {edu.institution} <br />
                  {/if}
                  {#if edu.description}
                    <strong>Description:</strong> {edu.description} <br /><br />
                  {/if}
                {/each}
              </ul>
            </ul>
          {/if}
          {#if resumeInterest.length > 0}
            <h2 class="bg-gray-100 print:text-xl">Interests</h2>
            <ul class="text-base leading-8 print:text-sm print:leading-6">
              <ul>
                {#each resumeInterest as interest}
                  <strong>Name:</strong>
                  {interest.name} <br />
                  {#if interest.description}
                    <strong>Description:</strong> {interest.description} <br /><br />
                  {/if}
                {/each}
              </ul>
            </ul>
          {/if}
          {#if resumeLanguage.length > 0}
            <h2 class="bg-gray-100 print:text-xl">Languages</h2>
            <ul class="text-base leading-8 print:text-sm print:leading-6">
              <ul>
                {#each resumeLanguage as lang}
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
          {#if resumeProject.length > 0}
            <h2 class="bg-gray-100 print:text-xl">Projects</h2>
            <ul class="text-base leading-8 print:text-sm print:leading-6">
              <ul>
                {#each resumeProject as project}
                  <strong>Title:</strong>
                  {project.title} <br />
                  {#if project.subtitle}
                    <strong>Subtitle:</strong> {project.subtitle} <br />
                  {/if}
                  {#if project.start_date}
                    <strong>Start Date:</strong> {project.start_date} <br />
                  {/if}
                  {#if project.end_date}
                    <strong>End Date:</strong> {project.end_date} <br />
                  {/if}
                  {#if project.description}
                    <strong>Description:</strong> {project.description} <br />
                  {/if}
                  <br />
                {/each}
              </ul>
            </ul>
          {/if}
          {#if resumePublication.length > 0}
            <h2 class="bg-gray-100 print:text-xl">Publications</h2>
            <ul class="text-base leading-8 print:text-sm print:leading-6">
              <ul>
                {#each resumePublication as publication}
                  <strong>Title:</strong>
                  {publication.title} <br />
                  {#if publication.publisher}
                    <strong>Publisher:</strong> {publication.publisher} <br />
                  {/if}
                  {#if publication.date}
                    <strong>Date:</strong> {publication.date} <br />
                  {/if}
                  {#if publication.description}
                    <strong>Description</strong> {publication.description} <br /><br />
                  {/if}
                {/each}
              </ul>
            </ul>
          {/if}
          {#if resumeReference.length > 0}
            <h2 class="bg-gray-100 print:text-xl">References</h2>
            <ul class="text-base leading-8 print:text-sm print:leading-6">
              <ul>
                {#each resumeReference as ref}
                  <strong>Name:</strong>
                  {ref.name} <br />
                  {#if ref.job_title}
                    <strong>Job Title:</strong> {ref.job_title} <br />
                  {/if}
                  {#if ref.organization}
                    <strong>Organization:</strong> {ref.organization} <br />
                  {/if}
                  {#if ref.email}
                    <strong>Email:</strong> {ref.email} <br />
                  {/if}
                  {#if ref.phone}
                    <strong>Phone:</strong> {ref.phone} <br /><br />
                  {/if}
                {/each}
              </ul>
            </ul>
          {/if}
        </Page>
      </div>
    </AppPdf>
  </section>
{/if}
