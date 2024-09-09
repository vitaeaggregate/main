<script lang="ts">
	import InputText from "$lib/components/InputText.svelte";

	let value = {
		value: "string",
		arrays: [
			{
				id: 1,
				hello: "There!"
			},
			{
				id: 2,
				hello: "there"
			}
		]
	};

	let arrays = value.arrays;

	let item = arrays[0];

	$: {
		arrays = arrays.map((value) => {
			if (item.id === value.id) return { ...item };
			else return value;
		});
	}

	$: {
		value = { ...value, arrays };
	}
</script>

<InputText bind:value={item.hello} />

{#each value.arrays as array}
	<p>{array.hello}</p>
{/each}

{#each arrays as array}
	<p>{array.hello}</p>
{/each}

<p>{item.hello}</p>
