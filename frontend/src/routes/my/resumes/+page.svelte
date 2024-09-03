<script lang="ts">
	import { account } from "$lib/store";
	import { createResume } from "$lib/api/resume";
	import type { BaseResume } from "$lib/interfaces/resume/Resume";
	import EducationExperience from "$lib/components/resume/Education.svelte";
	import Interests from "$lib/components/resume/Interest.svelte";
	import Links from "$lib/components/resume/Links.svelte";
	import PersonalInformation from "$lib/components/resume/PersonalInfo.svelte";
	import Publications from "$lib/components/resume/Publication.svelte";
	import Skills from "$lib/components/resume/Skill.svelte";
	import Awards from "$lib/components/resume/Award.svelte";
	import Certificates from "$lib/components/resume/Certificate.svelte";
	import Courses from "$lib/components/resume/Course.svelte";
	import Languages from "$lib/components/resume/Language.svelte";
	import ProfessionalExperience from "$lib/components/resume/ProfessionalExperience.svelte";
	import Projects from "$lib/components/resume/Project.svelte";
	import References from "$lib/components/resume/Reference.svelte";
	import InputText from "$lib/components/InputText.svelte";
	import type PersonalInfo from "$lib/interfaces/resume/PersonalInfo";
	import type Link from "$lib/interfaces/resume/Link";
	import type ProfessionalExp from "$lib/interfaces/resume/ProfessionalExp";
	import type Skill from "$lib/interfaces/resume/Skill";
	import type Education from "$lib/interfaces/resume/Education";
	import type Course from "$lib/interfaces/resume/Course";
	import type Language from "$lib/interfaces/resume/Language";
	import type Interest from "$lib/interfaces/resume/Interest";
	import type Project from "$lib/interfaces/resume/Project";
	import type Publication from "$lib/interfaces/resume/Publication";
	import type Award from "$lib/interfaces/resume/Award";
	import type Certificate from "$lib/interfaces/resume/Certificate";
	import type Reference from "$lib/interfaces/resume/Reference";

	export const id: number | null = null;

	let personalInfo: PersonalInfo | null = null;
	let profExp: ProfessionalExp | null = null;
	let link: Link | null = null;
	let skill: Skill | null = null;
	let education: Education | null = null;
	let course: Course | null = null;
	let language: Language | null = null;
	let interest: Interest | null = null;
	let project: Project | null = null;
	let publication: Publication | null = null;
	let award: Award | null = null;
	let certificate: Certificate | null = null;
	let reference: Reference | null = null;
	let title: string = "";

	async function handleSubmit() {
		if (!personalInfo || !$account) return;

		// const resumeObject: BaseResume = {
		// 	member: $account.id,
		// 	title: title,
		// 	personal: personalInfo,
		// 	professional_exps: profExp ? [profExp] : undefined,
		// 	links: link ? [link] : undefined,
		// 	skills: skill ? [skill] : undefined,
		// 	educations: education ? [education] : undefined,
		// 	courses: course ? [course] : undefined,
		// 	languages: language ? [language] : undefined,
		// 	interests: interest ? [interest] : undefined,
		// 	projects: project ? [project] : undefined,
		// 	publications: publication ? [publication] : undefined,
		// 	awards: award ? [award] : undefined,
		// 	certificates: certificate ? [certificate] : undefined,
		// 	references: reference ? [reference] : undefined
		// };

		const payload = {
			member: $account.id,
			title: "Accept such off act.",
			is_shareable: true,
			personal_info: {
				full_name:
					"Sea memory suggest guy. Lawyer culture fast forget officer. Shoulder event create air offer can now.",
				job_title: "Third marriage our affect best. Mr idea drug indicate different.",
				email: "mark06@example.org",
				phone_number: "874-563-5173x16",
				address: "076 Desiree Cape, New Laurenchester, AK 81224",
				date_of_birth: "1992-07-16",
				driving_license: "Determine last professional nor trip technology.",
				gender_pronoun: "They/Them",
				marital_status: "Single",
				nationality: "American"
			},
			links: [
				{
					title: "Song approach leg be agree record send firm.",
					url: "https://example.com/environment-employee"
				}
			],
			awards: [
				{
					title: "Central good radio free young general series.",
					issuer: "Night city wide again itself.",
					date: "1982-06-20",
					description:
						"Treatment several but away more chance. Safe reveal experience total message night."
				}
			],
			certificates: [
				{
					name: "About sign bring degree.",
					description:
						"Personal leave popular professional. Anything kind candidate represent book man item claim."
				}
			],
			languages: [
				{
					language: "Question free national property.",
					description: "TV sometimes consumer capital technology view.",
					skill_level: "Advanced"
				}
			],
			professional_exps: [
				{
					job_title: "Manager",
					employer: "Model bank question example list future.",
					city: "Colemanview",
					country: "Niue",
					start_date: "1974-09-15T08:53:10.820869Z",
					end_date: "2009-12-05T12:06:17.281772Z",
					description: "These here wish poor. Collection someone American."
				}
			],
			projects: [
				{
					title: "Single bad edge.",
					sub_title: "Federal dog activity.",
					start_date: "1980-07-02T06:26:45.286428Z",
					end_date: "1982-07-10T02:53:53.562045Z",
					description: "Several foot either its. Wonder into how everything whose."
				}
			],
			publications: [
				{
					title: "Language beat technology.",
					publisher: "Picture whole us important region collection.",
					date: "2009-05-13",
					description: "Economy build no respond project bring mention agency."
				},
				{
					title: "Upon near service price security fight.",
					publisher: "Society hot want. Others oil fast middle face seven almost sit.",
					date: "2016-01-15",
					description: "Experience heavy see your. Consider talk yes best him."
				},
				{
					id: 22,
					title: "Much arm particularly structure provide.",
					publisher: "Research husband choice hand him defense same.",
					date: "1989-01-22",
					description: "Local treat eye the sell let keep he."
				}
			],
			references: [
				{
					name: "Michael Torres",
					job_title: "Senior Manager",
					organization: "Nice Nature Language Inc.",
					email: "torresmichael@example.org",
					phone: "636-203-5897x847"
				},
				{
					name: "John Myers",
					job_title: "Civil Engineer",
					organization: "Early Ground Inc.",
					email: "myersjohn@example.com",
					phone: "(726)742-1715x094"
				},
				{
					name: "Christopher Case",
					job_title: "Project Lead",
					organization: "Firm Sing Trouble",
					email: "christophercase@example.net",
					phone: "001-816-208-0562x700"
				}
			],
			skills: [
				{
					name: "Education concern big argue.",
					description: "Second I ability. Economy window method democratic.",
					skill_level: "Advanced"
				}
			]
		};

		const resumeObject: BaseResume = payload;

		await createResume($account.id, resumeObject);
	}
</script>

<div>
	<h1>Resumes</h1>

	<PersonalInformation on:update={(event) => (personalInfo = event.detail)} />
	<Links on:update={(event) => (link = event.detail)} />
	<Skills on:update={(event) => (skill = event.detail)} />
	<ProfessionalExperience on:update={(event) => (profExp = event.detail)} />
	<EducationExperience on:update={(event) => (education = event.detail)} />
	<Courses on:update={(event) => (course = event.detail)} />
	<Languages on:update={(event) => (language = event.detail)} />
	<Interests on:update={(event) => (interest = event.detail)} />
	<Projects on:update={(event) => (project = event.detail)} />
	<Publications on:update={(event) => (publication = event.detail)} />
	<Awards on:update={(event) => (award = event.detail)} />
	<Certificates on:update={(event) => (certificate = event.detail)} />
	<References on:update={(event) => (reference = event.detail)} />

	<button on:click={handleSubmit}>Submit</button>
</div>
<!-- <Education></Education>
<Project></Project>
<Language></Language>
<Course></Course>
<Award></Award>
<ProfessionalExp></ProfessionalExp>
<Certificate></Certificate>
<Reference></Reference> -->
