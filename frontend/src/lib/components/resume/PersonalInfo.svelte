<script lang="ts">
  import InputText from "$lib/components/InputText.svelte";
  import InputDate from "$lib/components/InputDate.svelte";
  import type PersonalInfo from "$lib/interfaces/resume/PersonalInfo";
  import Modal from "../Modal.svelte";
	import Button from "../Button.svelte";

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
  let isModalHidden: boolean = true;
  // create a close function
  const closeModal = (event?: Event) => {
    if(event instanceof KeyboardEvent && event.key !== "Enter") return;
    isModalHidden = true;
  }
</script>

<div class="flex flex-col">
  <h2>Personal Info</h2>
  <InputText label="Full Name" required={true} bind:value={value.full_name} placeholder="Stephen A. Smith"/>
  <InputText label="Job Title" required={true} bind:value={value.job_title} placeholder="Fullstack Engineer"/>
  <InputText label="Email" bind:value={value.email} placeholder="stephen.smith@email.net"/>
  <InputText label="Phone Number" bind:value={value.phone_number} placeholder="XXX-XXXX-XXXX"/>
  <InputText label="Address" bind:value={value.address} placeholder="Tokyo, Japan"/>
  <InputDate label="Date of Birth" bind:value={value.date_of_birth}/>
  <div class="mt-2 mb-1">
    <Button on:click={() => (isModalHidden = false)}>More Info</Button>
  </div>
  {#if !isModalHidden}
    <Modal closeClick={closeModal}>
    <div>
      <div class="">
        <h2>More Info</h2>
      </div>
      <div class="">
        <div>
          <h3>Driving License</h3>
          <p>Some organizations require certain members to be able to travel. Specifying this can be useful for organizations.</p>
        </div>
        <div>

          <h3>Gender Pronouns</h3>
          <p>If you prefer specifying your pronouns, you are free to do so here</p>
        </div>
        <div>
          <h3>Visa Status</h3>
          <p>Specifying your visa status can help tip the scales for your candidacy or notify companies</p>
        </div>
        <div>
          <h3>Nationality</h3>
          <p>Specifying your nationality is sometimes useful information for companies choosing candidates</p>
        </div>
      </div>
    </div>
    </Modal>
  {/if}
  <InputText label="Driving License" bind:value={value.driving_license} placeholder="Yes"/>
  <InputText label="Gender Pronouns" bind:value={value.gender_pronoun} placeholder="He/Him"/>
  <InputText label="Marriage or Visa Status" bind:value={value.marital_status} placeholder="Marriage Visa"/>
  <InputText label="Nationality" bind:value={value.nationality} placeholder="USA"/>
</div>
