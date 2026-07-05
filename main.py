from agent import agent

print("=" * 50)
print("Smart File Agent")
print("Type 'exit' to quit.")
print("=" * 50)

while True:
    query = input("\n> ")

    if query.lower() == "exit":
        print("Goodbye!")
        break

    try:
        response = agent.run(query)
        print("\nResponse:\n")
        print(response)

    except Exception as e:
        print(f"\nError: {e}")