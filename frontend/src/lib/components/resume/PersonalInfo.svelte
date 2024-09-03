<script lang='ts'>
    import InputText from "$lib/components/InputText.svelte";
    import InputDate from "$lib/components/InputDate.svelte";
	import { createEventDispatcher } from "svelte";
	// import Page from "../../routes/+page.svelte";
    
    let headerId: number;
	let inputFullName: string;
	let inputJobTitle: string;
	let inputEmail: string;
	let inputPhoneNumber: string;
	let inputAddress: string;
	let inputDateOfBirth: Date;
	let inputDrivingLicense: string;
	let inputGenderPronoun: string;
	let inputMaritalStatus: string;
	let inputNationality: string;

    $: personalInfo = {
        header: headerId,
        full_name: inputFullName,
        job_title: inputJobTitle,
        email: inputEmail,
        phone_number: inputPhoneNumber,
        address: inputAddress,
        date_of_birth: inputDateOfBirth,
        driving_license: inputDrivingLicense,
        gender_pronoun: inputGenderPronoun,
        marital_status: inputMaritalStatus,
        nationality: inputNationality,
    }

    const dispatch = createEventDispatcher();
    $: {
        dispatch("update", personalInfo);
    }
</script>

<div class="flex flex-col">
    <h2>Personal Info</h2>
    <InputText label="Full Name" bind:value={inputFullName}/>
    <InputText label="Job Title" bind:value={inputJobTitle}/>
    <InputText label="Email" bind:value={inputEmail}/>
    <InputText label="Phone Number" bind:value={inputPhoneNumber}/>
    <InputText label="Address" bind:value={inputAddress}/>
    <InputDate label="Date of Birth" bind:value={inputDateOfBirth}/>
    <InputText label="Driving License" bind:value={inputDrivingLicense}/>
    <InputText label="Gender Pronouns" bind:value={inputGenderPronoun}/>
    <InputText label="Marital Status" bind:value={inputMaritalStatus}/>
    <InputText label="Nationality" bind:value={inputNationality}/>
</div>