from playwright.sync_api import sync_playwright, expect
class TestMCP:
    def test_add_todo_item(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()

            # Navigate to TodoMVC (React reference implementation)
            page.goto("https://todomvc.com/examples/react/dist/")

            # Locate the new-todo input and add an item
            new_todo_input = page.get_by_placeholder("What needs to be done?")
            new_todo_input.click()
            new_todo_input.fill("buy groceries")
            new_todo_input.press("Enter")

            # Assert the item appears in the todo list
            todo_list = page.locator(".todo-list li")
            expect(todo_list).to_have_count(1)
            expect(todo_list.first).to_contain_text("buy groceries")

            # Optional: assert the todo count label reflects 1 item left
            todo_count = page.locator(".todo-count")
            expect(todo_count).to_contain_text("1")

            print("Test passed: 'buy groceries' was successfully added.")

            browser.close()

if __name__ == "__main__":
    test = TestMCP()
    test.test_add_todo_item()