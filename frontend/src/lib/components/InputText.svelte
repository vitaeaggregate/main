<script context="module" lang="ts">
	export type InputType = "text" | "password";
</script>

<script lang="ts">
	export let label: string | null = null;
	export let placeholder: string | null = label;
	export let value: string = "";
	export let type: InputType = "text";
</script>

<label class="flex flex-col"
	>{label ? label + ":" : ""}
	{#if type === "text"}
		<input bind:value type="text" {placeholder} class="rounded-md border-2 p-1" />
	{:else if type === "password"}
		<input bind:value type="password" {placeholder} class="rounded-md border-2 p-1" />
	{/if}
</label>
