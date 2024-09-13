<script lang="ts">
  import InputText from "$lib/components/InputText.svelte";
  import InputDate from "$lib/components/InputDate.svelte";
  import type PersonalInfo from "$lib/interfaces/resume/PersonalInfo";

  export let value: PersonalInfo = {
    full_name: "",
    job_title: "",
    email: "",
    phone_number: "",
    address: "",
    date_of_birth: "",
    driving_license: "",
    gender_pronoun: "",
    marital_status: "",
    nationality: ""
  };
</script>

<div class="flex flex-col">
  <h2>Personal Info</h2>
  <InputText label="Full Name" required={true} bind:value={value.full_name} placeholder="Stephen A. Smith"/>
  <InputText label="Job Title" required={true} bind:value={value.job_title} placeholder="Fullstack Engineer"/>
  <InputText label="Email" bind:value={value.email} placeholder="stephen.smith@email.net"/>
  <InputText label="Phone Number" bind:value={value.phone_number} placeholder="XXX-XXXX-XXXX"/>
  <InputText label="Address" bind:value={value.address} placeholder="Tokyo, Japan"/>
  <InputDate label="Date of Birth" bind:value={value.date_of_birth}/>
  <InputText label="Driving License" bind:value={value.driving_license} placeholder="XXXXXXXXX"/>
  <InputText label="Gender Pronouns" bind:value={value.gender_pronoun} placeholder="He/Him"/>
  <InputText label="Marital Status" bind:value={value.marital_status} placeholder="Single"/>
  <InputText label="Nationality" bind:value={value.nationality} placeholder="USA"/>
</div>
