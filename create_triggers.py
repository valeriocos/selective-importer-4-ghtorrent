__author__ = 'valerio cosentino'

import database_manager as dbman


#the triggers are created to filter out the projects marked as "deleted",
#however other filters could be implemented (selecting a sub-set of projects, projects with more than X followers, etc.)
def main():
    dbman.execute_sql_statement("USE " + dbman.DATABASE)

    if dbman.check_table_exists('projects'):
        trigger_delete_insert_project = """DROP TRIGGER IF EXISTS insert_project;"""
        trigger_insert_project = """
        CREATE TRIGGER insert_project
        BEFORE INSERT
        ON projects FOR EACH ROW
        BEGIN
            IF NEW.deleted = 1 THEN
                SET NEW.id = -1;
            END IF;
        END;"""

        dbman.execute_sql_statement(trigger_delete_insert_project)
        dbman.execute_sql_statement(trigger_insert_project)

    if dbman.check_table_exists("issues"):
        trigger_delete_insert_issue = """DROP TRIGGER IF EXISTS insert_issue;"""
        trigger_insert_issue = """
        CREATE TRIGGER insert_issue
        BEFORE INSERT
        ON issues FOR EACH ROW
        BEGIN
            DECLARE project_found INTEGER;
            SELECT id INTO project_found
            FROM projects
            WHERE id = NEW.repo_id;
            IF (project_found IS NULL OR project_found = -1) THEN
                SET NEW.id = -1;
            END IF;
        END;"""
        dbman.execute_sql_statement(trigger_delete_insert_issue)
        dbman.execute_sql_statement(trigger_insert_issue)

    if dbman.check_table_exists("commits"):
        trigger_delete_insert_commit = """DROP TRIGGER IF EXISTS insert_commit;"""
        trigger_insert_commit = """
        CREATE TRIGGER insert_commit
        BEFORE INSERT
        ON commits FOR EACH ROW
        BEGIN
            DECLARE project_found INTEGER;
            SELECT id INTO project_found
            FROM projects
            WHERE id = NEW.project_id;
            IF (project_found IS NULL OR project_found = -1) THEN
                SET NEW.id = -1;
            END IF;
        END;"""
        dbman.execute_sql_statement(trigger_delete_insert_commit)
        dbman.execute_sql_statement(trigger_insert_commit)

    if dbman.check_table_exists("project_members"):
        trigger_delete_insert_project_member = """DROP TRIGGER IF EXISTS insert_project_member;"""
        trigger_insert_project_member = """
        CREATE TRIGGER insert_project_member
        BEFORE INSERT
        ON project_members FOR EACH ROW
        BEGIN
            DECLARE project_found INTEGER;
            SELECT id INTO project_found
            FROM projects
            WHERE id = NEW.repo_id;
            IF (project_found IS NULL OR project_found = -1) THEN
                SET NEW.repo_id = -1;
                SET NEW.user_id = -1;
            END IF;
        END;"""
        dbman.execute_sql_statement(trigger_delete_insert_project_member)
        dbman.execute_sql_statement(trigger_insert_project_member)

    if dbman.check_table_exists("watchers"):
        trigger_delete_insert_watcher = """DROP TRIGGER IF EXISTS insert_watcher;"""
        trigger_insert_watcher = """
        CREATE TRIGGER insert_watcher
        BEFORE INSERT
        ON watchers FOR EACH ROW
        BEGIN
            DECLARE project_found INTEGER;
            SELECT id INTO project_found
            FROM projects
            WHERE id = NEW.repo_id;
            IF (project_found IS NULL OR project_found = -1) THEN
                SET NEW.repo_id = -1;
                SET NEW.user_id = -1;
            END IF;
        END;"""
        dbman.execute_sql_statement(trigger_delete_insert_watcher)
        dbman.execute_sql_statement(trigger_insert_watcher)

    if dbman.check_table_exists("forks"):
        trigger_delete_insert_fork = """DROP TRIGGER IF EXISTS insert_fork;"""
        trigger_insert_fork = """
        CREATE TRIGGER insert_fork
        BEFORE INSERT
        ON forks FOR EACH ROW
        BEGIN
            DECLARE project_found INTEGER;
            SELECT id INTO project_found
            FROM projects
            WHERE id = NEW.forked_from_id;
            IF (project_found IS NULL OR project_found = -1) THEN
                SET NEW.fork_id = -1;
            END IF;
        END;"""
        dbman.execute_sql_statement(trigger_delete_insert_fork)
        dbman.execute_sql_statement(trigger_insert_fork)

    if dbman.check_table_exists("repo_labels"):
        trigger_delete_insert_repo_label = """DROP TRIGGER IF EXISTS insert_repo_label;"""
        trigger_insert_repo_label = """
        CREATE TRIGGER insert_repo_label
        BEFORE INSERT
        ON repo_labels FOR EACH ROW
        BEGIN
            DECLARE project_found INTEGER;
            SELECT id INTO project_found
            FROM projects
            WHERE id = NEW.repo_id;
            IF (project_found IS NULL OR project_found = -1) THEN
                SET NEW.id = -1;
            END IF;
        END;"""
        dbman.execute_sql_statement(trigger_delete_insert_repo_label)
        dbman.execute_sql_statement(trigger_insert_repo_label)

    if dbman.check_table_exists("repo_milestones"):
        trigger_delete_insert_repo_milestone = """DROP TRIGGER IF EXISTS insert_repo_milestone;"""
        trigger_insert_repo_milestone = """
        CREATE TRIGGER insert_repo_milestone
        BEFORE INSERT
        ON repo_milestones FOR EACH ROW
        BEGIN
            DECLARE project_found INTEGER;
            SELECT id INTO project_found
            FROM projects
            WHERE id = NEW.repo_id;
            IF (project_found IS NULL OR project_found = -1) THEN
                SET NEW.id = -1;
            END IF;
        END;"""
        dbman.execute_sql_statement(trigger_delete_insert_repo_milestone)
        dbman.execute_sql_statement(trigger_insert_repo_milestone)

    if dbman.check_table_exists("pull_requests"):
        trigger_delete_insert_pull_request = """DROP TRIGGER IF EXISTS insert_pull_request;"""
        trigger_insert_pull_request = """
        CREATE TRIGGER insert_pull_request
        BEFORE INSERT
        ON pull_requests FOR EACH ROW
        BEGIN
            DECLARE project_found INTEGER;
            SELECT id INTO project_found
            FROM projects
            WHERE id = NEW.base_repo_id;
            IF (project_found IS NULL OR project_found = -1) THEN
                SET NEW.id = -1;
            END IF;
        END;"""
        dbman.execute_sql_statement(trigger_delete_insert_pull_request)
        dbman.execute_sql_statement(trigger_insert_pull_request)

    if dbman.check_table_exists("project_commits"):
        trigger_delete_insert_project_commit = """DROP TRIGGER IF EXISTS insert_project_commit;"""
        trigger_insert_project_commit = """
        CREATE TRIGGER insert_project_commit
        BEFORE INSERT
        ON project_commits FOR EACH ROW
        BEGIN
            DECLARE project_found INTEGER;
            SELECT id INTO project_found
            FROM projects
            WHERE id = NEW.project_id;
            IF (project_found IS NULL OR project_found = -1) THEN
                SET NEW.project_id = -1;
                SET NEW.commit_id = -1;
            END IF;
        END;"""
        dbman.execute_sql_statement(trigger_delete_insert_project_commit)
        dbman.execute_sql_statement(trigger_insert_project_commit)

    if dbman.check_table_exists("commit_parents"):
        trigger_delete_insert_commit_parents = """DROP TRIGGER IF EXISTS insert_commit_parents;"""
        trigger_insert_commit_parents = """
        CREATE TRIGGER insert_commit_parents
        BEFORE INSERT
        ON commit_parents FOR EACH ROW
        BEGIN
            DECLARE commit_found INTEGER;
            DECLARE commit_parent_found INTEGER;

            SELECT id INTO commit_found
            FROM commits
            WHERE id = NEW.commit_id;

            SELECT id INTO commit_parent_found
            FROM commits
            WHERE id = NEW.parent_id;

            IF (commit_found IS NULL OR commit_found = -1 OR commit_parent_found IS NULL OR commit_parent_found = -1) THEN
                SET NEW.commit_id = -1;
                SET NEW.parent_id = -1;
            END IF;
        END;"""
        dbman.execute_sql_statement(trigger_delete_insert_commit_parents)
        dbman.execute_sql_statement(trigger_insert_commit_parents)

    if dbman.check_table_exists("commit_comments"):
        trigger_delete_insert_commit_comments = """DROP TRIGGER IF EXISTS insert_commit_comments;"""
        trigger_insert_commit_comments = """
        CREATE TRIGGER insert_commit_comments
        BEFORE INSERT
        ON commit_comments FOR EACH ROW
        BEGIN
            DECLARE commit_found INTEGER;

            SELECT id INTO commit_found
            FROM commits
            WHERE id = NEW.commit_id;

            IF (commit_found IS NULL OR commit_found = -1) THEN
                SET NEW.id = -1;
            END IF;
        END;"""
        dbman.execute_sql_statement(trigger_delete_insert_commit_comments)
        dbman.execute_sql_statement(trigger_insert_commit_comments)

    if dbman.check_table_exists("pull_request_history"):
        trigger_delete_insert_pull_request_history = """DROP TRIGGER IF EXISTS insert_pull_request_history;"""
        trigger_insert_pull_request_history = """
        CREATE TRIGGER insert_pull_request_history
        BEFORE INSERT
        ON pull_request_history FOR EACH ROW
        BEGIN
            DECLARE pull_request_found INTEGER;
            SELECT id INTO pull_request_found
            FROM pull_requests
            WHERE id = NEW.pull_request_id;
            IF (pull_request_found IS NULL OR pull_request_found = -1) THEN
                SET NEW.id = -1;
            END IF;
        END;"""
        dbman.execute_sql_statement(trigger_delete_insert_pull_request_history)
        dbman.execute_sql_statement(trigger_insert_pull_request_history)

    if dbman.check_table_exists("pull_request_comments"):
        trigger_delete_insert_pull_request_comment = """DROP TRIGGER IF EXISTS insert_pull_request_comment;"""
        trigger_insert_pull_request_comment = """
        CREATE TRIGGER insert_pull_request_comment
        BEFORE INSERT
        ON pull_request_comments FOR EACH ROW
        BEGIN
            DECLARE pull_request_found INTEGER;
            SELECT id INTO pull_request_found
            FROM pull_requests
            WHERE id = NEW.pull_request_id;
            IF (pull_request_found IS NULL OR pull_request_found = -1) THEN
                SET NEW.comment_id = -1;
            END IF;
        END;"""
        dbman.execute_sql_statement(trigger_delete_insert_pull_request_comment)
        dbman.execute_sql_statement(trigger_insert_pull_request_comment)

    if dbman.check_table_exists("pull_request_commits"):
        trigger_delete_insert_pull_request_commit = """DROP TRIGGER IF EXISTS insert_pull_request_commit;"""
        trigger_insert_pull_request_commit = """
        CREATE TRIGGER insert_pull_request_commit
        BEFORE INSERT
        ON pull_request_commits FOR EACH ROW
        BEGIN
            DECLARE pull_request_found INTEGER;
            SELECT id INTO pull_request_found
            FROM pull_requests
            WHERE id = NEW.pull_request_id;
            IF (pull_request_found IS NULL OR pull_request_found = -1) THEN
                SET NEW.pull_request_id = -1;
                SET NEW.commit_id = -1;
            END IF;
        END;"""
        dbman.execute_sql_statement(trigger_delete_insert_pull_request_commit)
        dbman.execute_sql_statement(trigger_insert_pull_request_commit)

    if dbman.check_table_exists("issue_labels"):
        trigger_delete_insert_issue_label = """DROP TRIGGER IF EXISTS insert_issue_label;"""
        trigger_insert_issue_label = """
        CREATE TRIGGER insert_issue_label
        BEFORE INSERT
        ON issue_labels FOR EACH ROW
        BEGIN
            DECLARE issue_found INTEGER;
            SELECT id INTO issue_found
            FROM issues
            WHERE id = NEW.issue_id;
            IF (issue_found IS NULL OR issue_found = -1) THEN
                SET NEW.issue_id = -1;
                SET NEW.label_id = -1;
            END IF;
        END;"""
        dbman.execute_sql_statement(trigger_delete_insert_issue_label)
        dbman.execute_sql_statement(trigger_insert_issue_label)

    if dbman.check_table_exists("issue_events"):
        trigger_delete_insert_issue_event = """DROP TRIGGER IF EXISTS insert_issue_event;"""
        trigger_insert_issue_event = """
        CREATE TRIGGER insert_issue_event
        BEFORE INSERT
        ON issue_events FOR EACH ROW
        BEGIN
            DECLARE issue_found INTEGER;
            SELECT id INTO issue_found
            FROM issues
            WHERE id = NEW.issue_id;
            IF (issue_found IS NULL OR issue_found = -1) THEN
                SET NEW.event_id = -1;
            END IF;
        END;"""
        dbman.execute_sql_statement(trigger_delete_insert_issue_event)
        dbman.execute_sql_statement(trigger_insert_issue_event)

    if dbman.check_table_exists("issue_comments"):
        trigger_delete_insert_issue_comment = """DROP TRIGGER IF EXISTS insert_issue_comment;"""
        trigger_insert_issue_comment = """
        CREATE TRIGGER insert_issue_comment
        BEFORE INSERT
        ON issue_comments FOR EACH ROW
        BEGIN
            DECLARE issue_found INTEGER;
            SELECT id INTO issue_found
            FROM issues
            WHERE id = NEW.issue_id;
            IF (issue_found IS NULL OR issue_found = -1) THEN
                SET NEW.comment_id = -1;
            END IF;
        END;"""
        dbman.execute_sql_statement(trigger_delete_insert_issue_comment)
        dbman.execute_sql_statement(trigger_insert_issue_comment)

    dbman.close_connection()


if __name__ == "__main__":
    main()