import re

import automatic_code_review_commons as commons


def review(config):
    merge = config['merge']
    configs = config['configs']
    labels_in_merge = merge['labels']
    branch = merge['branch']['target']

    comments = []

    for config_obj in configs:
        if "authors" in config_obj and merge['author'] not in config_obj["authors"]:
            continue

        if "branches" in config_obj and not __verify_regex_list(config_obj['branches'], branch):
            continue

        labels = config_obj['labels']

        for label in labels:
            if label not in labels_in_merge:
                description = config_obj['description'].replace("${LABEL}", label)

                comments.append(commons.comment_create(
                    comment_id=commons.comment_generate_id(description),
                    comment_path=None,
                    comment_description=description,
                    comment_snipset=False,
                ))

    print(comments)

    return comments


def __verify_regex_list(regex_list, branch):
    for regex in regex_list:
        if re.match(regex, branch):
            return True

    return False
