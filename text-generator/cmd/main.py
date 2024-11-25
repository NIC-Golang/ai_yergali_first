from internal.core.usecases.gen_tags import generate_tags

def main():
    reviews = ["Прекрасная книга о жизни", "Очень интересный сюжет", "Автор мастерски описал персонажей"]
    tag_generator = generate_tags(threshold=0.8)
    tag_generator.execute(reviews=reviews)


if __name__ == "__main__":
    main()