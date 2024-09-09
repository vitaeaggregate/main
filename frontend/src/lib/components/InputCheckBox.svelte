<script lang="ts">
	export let label: string | null = null;
	export let value: boolean = false;
</script>

<label class="flex">
	<input type="checkbox" bind:checked={value} class="mt-0.5" />
	<span class="mx-2">{label ? label : ""}</span>
</label>
